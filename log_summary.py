import csv
from datetime import datetime, timedelta
from collections import defaultdict
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan


ES_HOST = '192.168.100.71' 
ES_PORT = 30092 
ES_USER = None 
ES_PASSWORD = None 

ES_INDEX_PATTERN = 'beats-*' 



output_file = 'log_summary.csv'

def get_log_time_range():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1) 
    print(f"✅ ログ検索期間: {start_time.strftime('%Y-%m-%d %H:%M:%S')} から {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    return start_time, end_time

def get_logs_from_elasticsearch(start_time, end_time):
    es = Elasticsearch(
        hosts=[{'host': ES_HOST, 'port': ES_PORT, 'scheme': 'http'}],
        http_auth=(ES_USER, ES_PASSWORD) if ES_USER and ES_PASSWORD else None,
        request_timeout=60, 
        verify_certs=False 
    )

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
        for hit in scan(es,
                        query=query,
                        index=ES_INDEX_PATTERN,
                        scroll='2m',
                        timeout='60s' 
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

            # 5分ごとに丸める
            minute = (timestamp.minute // 5) * 5
            rounded_time = timestamp.replace(minute=minute, second=0, microsecond=0)

            key = f"{rounded_time.strftime('%Y-%m-%d %H:%M')} {container_name}"
            counter[key] += 1

        except ValueError as e:
            print(f"エラー: タイムスタンプのパースに失敗しました - {e} → {timestamp_str}")
            continue

    last_interval_counts = {}

    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['時間帯', 'コンテナ名', 'ログ件数', '前時間帯からの変化'])

        for key, current_count in sorted(counter.items()):
            time_str, container_name = key.rsplit(' ', 1) 

            change_str = "-" 
            comparison_key = f"{time_str}_{container_name}"

            if container_name in last_interval_counts:
                previous_count = last_interval_counts[container_name]
                change = current_count - previous_count
                change_str = f"{change:+d}" 

            last_interval_counts[container_name] = current_count

            writer.writerow([time_str, container_name, current_count, change_str])

    print(f"✅ 集計が完了しました → {output_file}")
