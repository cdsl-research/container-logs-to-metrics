# container-logs-to-metrics

## 構成
```
/home/c0a22166/teian
├── log_summary.py
```

## 実行する環境
- Python verion：3.12.3

## プログラムの概要

### `log_summary.py`
**説明**:このファイルをPythonで動かすことで、Elasticsearchのbeats indexにあるログをコンテナ名別に5分ごとに時間帯を分けて出力されます。出力されるログはプログラム実行時の１時間前から現在時刻までのログです。
- 入力は，Elasticsearchのbeats indexのログです。出力はプログラム実行時の１時間前から現在時刻までのログです。
- 出力では、ログの時間帯、コンテナ名、ログ件数、5分前のログ件数からの変化を出力します。
  
**使い方**:
<img width="1060" height="146" alt="image" src="https://github.com/user-attachments/assets/e4062162-a5e0-47c2-a26b-4b1a602fc56e" />


**実行結果**

<img width="769" height="318" alt="image" src="https://github.com/user-attachments/assets/669359b4-623a-4a7a-9453-8a4dea47b1e8" />

**注意**
- elasticserchモジュールをインストールする必要があります。
  - インストールされていない場合は下記のコマンドを入力して、コマンドを実行して下さい。
```
# 仮想環境の作成
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate

# elasticsearchパッケージのインストール
pip install elasticsearch
```
- 集計したいログのindexを変更するには、log_summary.pyの以下の部分を変更してください。（log_summary.pyの14行目）
  - 'beats-*'の部分を変更することで集計するindexを変更することができます。
```
ES_INDEX_PATTERN = 'beats-*'
```
- 集計の期間を変更するには、log_summary.pyの以下の部分を変更してください。（log_summary.pyの22行目）
  - ()の中をweek=1にすることで1週間、minutes=30にすることで30分間というように変更できます。
```
start_time = end_time - timedelta(hours=1)
```
- 集計の頻度を変更するには、log_summary.pyの以下の部分を変更してください。（log_summary.pyの88、89行目）
  - minute = timestamp.minuteの状態だと1分ごと集計されます。
  - minute = (timestamp.minute // 15) * 15にすることで15分ごとに集計されます。
  - hour = (timestamp.hour // 2) * 2にすることで2時間ごとに集計されます。
```
minute = (timestamp.minute // 5) * 5
rounded_time = timestamp.replace(minute=minute, second=0, microsecond=0)
```
