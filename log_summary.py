import csv
from datetime import datetime, timedelta
from collections import defaultdict
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

# --- 設定 ---
# Elasticsearch接続情報
# ここにElasticsearchサーバーのIPアドレスとポート、認証情報を直接指定します。
# 認証が不要な場合は ES_USER と ES_PASSWORD は None のままにしてください。
ES_HOST = '192.168.100.71' # ★確認したIPアドレスに修正済み★
ES_PORT = 30092          # ★確認したポート番号に修正済み★
ES_USER = None          # ★認証が必要な場合は 'your_username' のようにユーザー名を指定★
ES_PASSWORD = None      # ★認証が必要な場合は 'your_password' のようにパスワードを指定★

# Elasticsearchのインデックスパターン
# curlコマンドの出力から、あなたのログのインデックスパターンを特定し、設定します。
# 例: 'weblog-*', 'beats-*', または両方を含める 'weblog-*,beats-*'
ES_INDEX_PATTERN = 'beats-*' # ★あなたの環境に最も合うインデックスパターンに修正してください★
                              # 例として 'beats-*' を入れています。
                              # もしweblog系のログも集計したいなら 'weblog-*,beats-*' に変更
                              # 複数のパターンを指定する場合はカンマ区切りです。

# ログ出力ファイル
output_file = 'log_summary.csv'

# --- ログ取得期間の決定 ---
# ここでは例として過去24時間分のログを取得します。
# 実際にはRedmineやPrometheusから障害発生期間を取得するロジックをここに実装します。
def get_log_time_range():
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1) # 過去24時間分のログ
    print(f"✅ ログ検索期間: {start_time.strftime('%Y-%m-%d %H:%M:%S')} から {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    return start_time, end_time

# --- Elasticsearchからログを取得する関数 ---
def get_logs_from_elasticsearch(start_time, end_time):
    # Elasticsearchクライアントの初期化
    es = Elasticsearch(
        hosts=[{'host': ES_HOST, 'port': ES_PORT, 'scheme': 'http'}], 
        http_auth=(ES_USER, ES_PASSWORD) if ES_USER and ES_PASSWORD else None,
        request_timeout=60, # リクエストのタイムアウトを長めに設定 (秒)
        verify_certs=False # SSL証明書の検証が必要な場合は True に設定し、適切な cert_path を指定
    )

    # ログ検索クエリ
    query = {
        "query": {
            "range": {
                "@timestamp": {
                    "gte": start_time.isoformat(timespec='milliseconds') + 'Z',
                    "lte": end_time.isoformat(timespec='milliseconds') + 'Z'
                }
            }
        },
        "sort": [
            {"@timestamp": {"order": "asc"}}
        ]
    }

    print(f"✅ Elasticsearch ({ES_HOST}:{ES_PORT}, Index: {ES_INDEX_PATTERN}) からログを取得中...")
    
    logs = []
    try:
        # scan ヘルパー関数を使って、効率的に大量のドキュメントをスクロール取得
        for hit in scan(es,
                        query=query,
                        index=ES_INDEX_PATTERN,
                        scroll='2m',
                        timeout='60s' # scanヘルパーのtimeoutはrequest_timeoutとは別なのでそのまま
                        ):
            source = hit['_source']
            logs.append({
                '@timestamp': source.get('@timestamp'),
                'kubernetes.container.name': source.get('kubernetes', {}).get('container', {}).get('name')
            })
    except Exception as e:
        print(f"❌ Elasticsearchからのログ取得中にエラーが発生しました: {e}")
        return []

    print(f"✅ {len(logs)} 件のログを取得しました。")
    return logs

# --- メイン処理 ---
if __name__ == "__main__":
    counter = defaultdict(int)

    log_start_time, log_end_time = get_log_time_range()
    log_entries = get_logs_from_elasticsearch(log_start_time, log_end_time)

    for row in log_entries:
        timestamp_str = row.get('@timestamp')
        container_name = row.get('kubernetes.container.name')

        if not timestamp_str or not container_name:
            continue

        try:
            timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
            timestamp = timestamp.replace(tzinfo=None)

            minute = (timestamp.minute // 15) * 15
            rounded_time = timestamp.replace(minute=minute, second=0, microsecond=0)

            key = f"{rounded_time.strftime('%Y-%m-%d %H:%M')} {container_name}"
            counter[key] += 1

        except ValueError as e:
            print(f"エラー: タイムスタンプのパースに失敗しました - {e} → {timestamp_str}")
            continue

    # 各コンテナの前の時間帯のログ件数を保持する辞書
    last_interval_counts = {}

    # 集計結果をCSVに出力
    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # ヘッダー行に「前時間帯からの変化」を追加
        writer.writerow(['時間帯', 'コンテナ名', 'ログ件数', '前時間帯からの変化'])

        # 集計結果を時間帯とコンテナ名でソートして処理
        for key, current_count in sorted(counter.items()):
            time_str, container_name = key.rsplit(' ', 1) # キーを時間とコンテナ名に分割
            
            change_str = "-" # 初回または前のデータがない場合はハイフン

            if container_name in last_interval_counts:
                previous_count = last_interval_counts[container_name]
                change = current_count - previous_count
                change_str = f"{change:+d}" # 例: "+10", "-5" のように符号付きで表示
            
            # 現在の件数を次の比較のために保存
            last_interval_counts[container_name] = current_count

            writer.writerow([time_str, container_name, current_count, change_str])

    print(f"✅ 集計が完了しました → {output_file}")
