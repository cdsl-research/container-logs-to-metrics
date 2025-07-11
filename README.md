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
- 入力は，Elasticsearchのbeats indexのログである。出力はプログラム実行時の１時間前から現在時刻までのログです。
- 出力では、ログの時間帯、コンテナ名、ログ件数、5分前のログ件数からの変化を出力します。
  
**使い方**:
```
c0a22166@c0a22166:~/teian$ source venv/bin/activate
(venv) c0a22166@c0a22166:~/teian$ python3 log_summary.py
✅ ログ検索期間: 2025-07-11 00:40:42 から 2025-07-11 01:40:42
✅ Elasticsearch (192.168.100.71:30092, Index: beats-*) からログを取得中...
✅ 570673 件のログを取得しました。
✅ 集計が完了しました → log_summary.csv
(venv) c0a22166@c0a22166:~/teian$ 
```
**実行結果**
```
(venv) c0a22166@c0a22166:~/teian$ cat log_summary.csv
時間帯,コンテナ名,ログ件数,前時間帯からの変化
2025-07-11 02:25,author-app-container,362,-
2025-07-11 02:25,author-mongo-container,3,-
2025-07-11 02:25,builder,78,-
2025-07-11 02:25,cadvisor,1,-
2025-07-11 02:25,ceph-exporter,301,-
2025-07-11 02:25,coredns,46,-
2025-07-11 02:25,csi-resizer,2,-
2025-07-11 02:25,csi-snapshotter,68,-
2025-07-11 02:25,discovery,2,-
2025-07-11 02:25,filebeat,967,-
2025-07-11 02:25,front-app-container,810,-
2025-07-11 02:25,istio-proxy,1665,-
2025-07-11 02:25,jaeger,6,-
2025-07-11 02:25,kea,66,-
2025-07-11 02:25,log-collector,53,-
2025-07-11 02:25,metrics,75,-
2025-07-11 02:25,mgr,375,-
2025-07-11 02:25,mon,2896,-
2025-07-11 02:25,my-redmine,160,-
2025-07-11 02:25,osd,13,-
2025-07-11 02:25,paper-app-container,168,-
2025-07-11 02:25,paper-mongo-container,3,-
2025-07-11 02:25,prometheus,19,-
2025-07-11 02:25,stats-app-container,13765,-
2025-07-11 02:25,stns-server,199,-
2025-07-11 02:25,vmware-exporter,5307,-
2025-07-11 02:25,watch-active,147,-
2025-07-11 02:30,author-app-container,550,+188
2025-07-11 02:30,author-mongo-container,5,+2
2025-07-11 02:30,builder,130,+52
2025-07-11 02:30,cadvisor,2,+1
2025-07-11 02:30,ceph-exporter,477,+176
2025-07-11 02:30,coredns,74,+28
2025-07-11 02:30,csi-snapshotter,112,+44
2025-07-11 02:30,discovery,24,+22
2025-07-11 02:30,filebeat,2206,+1239
2025-07-11 02:30,front-app-container,1446,+636
2025-07-11 02:30,fulltext-app-container,277,-
2025-07-11 02:30,grafana,1,-
2025-07-11 02:30,istio-proxy,2637,+972
2025-07-11 02:30,kea,98,+32
2025-07-11 02:30,log-collector,110,+57
2025-07-11 02:30,metrics,120,+45
2025-07-11 02:30,mgr,601,+226
2025-07-11 02:30,mon,4435,+1539
2025-07-11 02:30,my-redmine,250,+90
2025-07-11 02:30,osd,637,+624
2025-07-11 02:30,paper-app-container,275,+107
2025-07-11 02:30,paper-mongo-container,5,+2
2025-07-11 02:30,prometheus,30,+11
2025-07-11 02:30,stats-app-container,22230,+8465
2025-07-11 02:30,stns-server,317,+118
2025-07-11 02:30,vmware-exporter,8457,+3150
2025-07-11 02:30,watch-active,228,+81
2025-07-11 02:35,author-app-container,554,+4
2025-07-11 02:35,author-mongo-container,6,+1
2025-07-11 02:35,builder,126,-4
2025-07-11 02:35,cadvisor,2,+0
2025-07-11 02:35,ceph-exporter,479,+2
2025-07-11 02:35,coredns,78,+4
2025-07-11 02:35,csi-resizer,2,+0
2025-07-11 02:35,csi-snapshotter,106,-6
2025-07-11 02:35,discovery,32,+8
2025-07-11 02:35,filebeat,2206,+0
2025-07-11 02:35,front-app-container,1441,-5
2025-07-11 02:35,fulltext-app-container,147,-130
2025-07-11 02:35,grafana,2,+1
2025-07-11 02:35,istio-proxy,2631,-6
2025-07-11 02:35,kea,91,-7
2025-07-11 02:35,log-collector,239,+129
2025-07-11 02:35,metrics,119,-1
2025-07-11 02:35,mgr,604,+3
2025-07-11 02:35,mon,4617,+182
2025-07-11 02:35,my-redmine,250,+0
2025-07-11 02:35,osd,354,-283
2025-07-11 02:35,paper-app-container,265,-10
2025-07-11 02:35,paper-mongo-container,11,+6
2025-07-11 02:35,prometheus,30,+0
2025-07-11 02:35,redmine-ticket-receiver,1,-
2025-07-11 02:35,stats-app-container,22115,-115
2025-07-11 02:35,stns-server,317,+0
2025-07-11 02:35,vmware-exporter,8468,+11
2025-07-11 02:35,watch-active,234,+6
2025-07-11 02:40,author-app-container,540,-14
2025-07-11 02:40,author-mongo-container,5,-1
2025-07-11 02:40,builder,126,+0
2025-07-11 02:40,cadvisor,2,+0
2025-07-11 02:40,ceph-exporter,478,-1
2025-07-11 02:40,coredns,76,-2
2025-07-11 02:40,csi-snapshotter,104,-2
2025-07-11 02:40,discovery,44,+12
2025-07-11 02:40,filebeat,2207,+1
2025-07-11 02:40,front-app-container,1443,+2
2025-07-11 02:40,fulltext-app-container,395,+248
2025-07-11 02:40,istio-proxy,2634,+3
2025-07-11 02:40,jumpsv,9,-
2025-07-11 02:40,kea,93,+2
2025-07-11 02:40,log-collector,53,-186
2025-07-11 02:40,metrics,118,-1
2025-07-11 02:40,mgr,601,-3
2025-07-11 02:40,mon,4576,-41
2025-07-11 02:40,my-redmine,250,+0
2025-07-11 02:40,osd,233,-121
2025-07-11 02:40,paper-app-container,274,+9
2025-07-11 02:40,paper-mongo-container,5,-6
2025-07-11 02:40,prometheus,30,+0
2025-07-11 02:40,recu-pdns-recursor-helm,6,-
2025-07-11 02:40,stats-app-container,22119,+4
2025-07-11 02:40,stns-server,358,+41
2025-07-11 02:40,vmware-exporter,8452,-16
2025-07-11 02:40,watch-active,240,+6
2025-07-11 02:45,author-app-container,567,+27
2025-07-11 02:45,author-mongo-container,5,+0
2025-07-11 02:45,builder,130,+4
2025-07-11 02:45,cadvisor,2,+0
2025-07-11 02:45,ceph-exporter,477,-1
2025-07-11 02:45,coredns,76,+0
2025-07-11 02:45,csi-resizer,2,+0
2025-07-11 02:45,csi-snapshotter,110,+6
2025-07-11 02:45,discovery,30,-14
2025-07-11 02:45,filebeat,2183,-24
2025-07-11 02:45,front-app-container,1447,+4
2025-07-11 02:45,fulltext-app-container,393,-2
2025-07-11 02:45,grafana,4,+2
2025-07-11 02:45,istio-proxy,2639,+5
2025-07-11 02:45,kea,94,+1
2025-07-11 02:45,log-collector,110,+57
2025-07-11 02:45,metrics,118,+0
2025-07-11 02:45,mgr,602,+1
2025-07-11 02:45,mon,4359,-217
2025-07-11 02:45,my-redmine,250,+0
2025-07-11 02:45,osd,21,-212
2025-07-11 02:45,paper-app-container,269,-5
2025-07-11 02:45,paper-mongo-container,5,+0
2025-07-11 02:45,powerdns-helm,1,-
2025-07-11 02:45,prometheus,30,+0
2025-07-11 02:45,stats-app-container,22002,-117
2025-07-11 02:45,stns-server,317,-41
2025-07-11 02:45,vmware-exporter,8465,+13
2025-07-11 02:45,watch-active,228,-12
2025-07-11 02:50,author-app-container,547,-20
2025-07-11 02:50,author-mongo-container,5,+0
2025-07-11 02:50,builder,126,-4
2025-07-11 02:50,cadvisor,2,+0
2025-07-11 02:50,ceph-exporter,478,+1
2025-07-11 02:50,coredns,74,-2
2025-07-11 02:50,csi-snapshotter,110,+0
2025-07-11 02:50,discovery,14,-16
2025-07-11 02:50,filebeat,2214,+31
2025-07-11 02:50,front-app-container,1444,-3
2025-07-11 02:50,fulltext-app-container,26,-367
2025-07-11 02:50,istio-proxy,2638,-1
2025-07-11 02:50,jumpsv,2,-7
2025-07-11 02:50,kea,98,+4
2025-07-11 02:50,log-collector,239,+129
2025-07-11 02:50,metrics,119,+1
2025-07-11 02:50,mgr,602,+0
2025-07-11 02:50,mon,4838,+479
2025-07-11 02:50,my-redmine,250,+0
2025-07-11 02:50,osd,584,+563
2025-07-11 02:50,paper-app-container,271,+2
2025-07-11 02:50,paper-mongo-container,5,+0
2025-07-11 02:50,prometheus,30,+0
2025-07-11 02:50,stats-app-container,22117,+115
2025-07-11 02:50,stns-server,319,+2
2025-07-11 02:50,vmware-exporter,8459,-6
2025-07-11 02:50,watch-active,234,+6
2025-07-11 02:55,author-app-container,577,+30
2025-07-11 02:55,author-mongo-container,5,+0
2025-07-11 02:55,builder,127,+1
2025-07-11 02:55,cadvisor,2,+0
2025-07-11 02:55,ceph-exporter,478,+0
2025-07-11 02:55,coredns,76,+2
2025-07-11 02:55,csi-resizer,2,+0
2025-07-11 02:55,csi-snapshotter,102,-8
2025-07-11 02:55,discovery,8,-6
2025-07-11 02:55,filebeat,2168,-46
2025-07-11 02:55,front-app-container,1291,-153
2025-07-11 02:55,fulltext-app-container,386,+360
2025-07-11 02:55,grafana,2,-2
2025-07-11 02:55,istio-proxy,2629,-9
2025-07-11 02:55,jumpsv,5,+3
2025-07-11 02:55,kea,92,-6
2025-07-11 02:55,log-collector,53,-186
2025-07-11 02:55,metrics,118,-1
2025-07-11 02:55,mgr,602,+0
2025-07-11 02:55,mon,4232,-606
2025-07-11 02:55,my-redmine,250,+0
2025-07-11 02:55,osd,21,-563
2025-07-11 02:55,paper-app-container,272,+1
2025-07-11 02:55,paper-mongo-container,5,+0
2025-07-11 02:55,prometheus,30,+0
2025-07-11 02:55,stats-app-container,22004,-113
2025-07-11 02:55,stns-server,342,+23
2025-07-11 02:55,vmware-exporter,8456,-3
2025-07-11 02:55,watch-active,232,-2
2025-07-11 03:00,author-app-container,578,+1
2025-07-11 03:00,author-mongo-container,5,+0
2025-07-11 03:00,builder,127,+0
2025-07-11 03:00,cadvisor,2,+0
2025-07-11 03:00,ceph-exporter,477,-1
2025-07-11 03:00,coredns,76,+0
2025-07-11 03:00,csi-snapshotter,106,+4
2025-07-11 03:00,discovery,32,+24
2025-07-11 03:00,filebeat,2783,+615
2025-07-11 03:00,front-app-container,1444,+153
2025-07-11 03:00,fulltext-app-container,281,-105
2025-07-11 03:00,grafana,1,-1
2025-07-11 03:00,istio-proxy,2641,+12
2025-07-11 03:00,kea,100,+8
2025-07-11 03:00,log-collector,110,+57
2025-07-11 03:00,metrics,118,+0
2025-07-11 03:00,mgr,601,-1
2025-07-11 03:00,mon,4710,+478
2025-07-11 03:00,my-redmine,250,+0
2025-07-11 03:00,osd,544,+523
2025-07-11 03:00,paper-app-container,267,-5
2025-07-11 03:00,paper-mongo-container,6,+1
2025-07-11 03:00,prometheus,34,+4
2025-07-11 03:00,stats-app-container,21933,-71
2025-07-11 03:00,stns-server,317,-25
2025-07-11 03:00,vmware-exporter,8460,+4
2025-07-11 03:00,watch-active,233,+1
2025-07-11 03:05,author-app-container,572,-6
2025-07-11 03:05,author-mongo-container,5,+0
2025-07-11 03:05,builder,126,-1
2025-07-11 03:05,cadvisor,2,+0
2025-07-11 03:05,ceph-exporter,478,+1
2025-07-11 03:05,coredns,78,+2
2025-07-11 03:05,csi-resizer,2,+0
2025-07-11 03:05,csi-snapshotter,108,+2
2025-07-11 03:05,ddns,10,-
2025-07-11 03:05,discovery,26,-6
2025-07-11 03:05,filebeat,2229,-554
2025-07-11 03:05,front-app-container,1443,-1
2025-07-11 03:05,fulltext-app-container,131,-150
2025-07-11 03:05,grafana,2,+1
2025-07-11 03:05,istio-proxy,2630,-11
2025-07-11 03:05,kea,91,-9
2025-07-11 03:05,log-collector,239,+129
2025-07-11 03:05,metrics,117,-1
2025-07-11 03:05,mgr,604,+3
2025-07-11 03:05,mon,4601,-109
2025-07-11 03:05,my-redmine,250,+0
2025-07-11 03:05,osd,20,-524
2025-07-11 03:05,paper-app-container,275,+8
2025-07-11 03:05,paper-mongo-container,8,+2
2025-07-11 03:05,prometheus,30,-4
2025-07-11 03:05,stats-app-container,22233,+300
2025-07-11 03:05,stns-server,317,+0
2025-07-11 03:05,vmware-exporter,8465,+5
2025-07-11 03:05,watch-active,234,+1
2025-07-11 03:10,author-app-container,576,+4
2025-07-11 03:10,author-mongo-container,5,+0
2025-07-11 03:10,builder,126,+0
2025-07-11 03:10,cadvisor,2,+0
2025-07-11 03:10,ceph-exporter,477,-1
2025-07-11 03:10,coredns,72,-6
2025-07-11 03:10,csi-snapshotter,104,-4
2025-07-11 03:10,ddns,10,+0
2025-07-11 03:10,discovery,30,+4
2025-07-11 03:10,filebeat,2183,-46
2025-07-11 03:10,front-app-container,1447,+4
2025-07-11 03:10,fulltext-app-container,394,+263
2025-07-11 03:10,istio-proxy,2641,+11
2025-07-11 03:10,kea,93,+2
2025-07-11 03:10,log-collector,53,-186
2025-07-11 03:10,metrics,118,+1
2025-07-11 03:10,mgr,601,-3
2025-07-11 03:10,mon,4446,-155
2025-07-11 03:10,my-redmine,250,+0
2025-07-11 03:10,osd,301,+281
2025-07-11 03:10,paper-app-container,269,-6
2025-07-11 03:10,paper-mongo-container,5,-3
2025-07-11 03:10,prometheus,30,+0
2025-07-11 03:10,recu-pdns-recursor-helm,6,+0
2025-07-11 03:10,stats-app-container,22002,-231
2025-07-11 03:10,stns-server,318,+1
2025-07-11 03:10,vmware-exporter,8460,-5
2025-07-11 03:10,watch-active,231,-3
2025-07-11 03:15,author-app-container,561,-15
2025-07-11 03:15,author-mongo-container,5,+0
2025-07-11 03:15,builder,125,-1
2025-07-11 03:15,cadvisor,2,+0
2025-07-11 03:15,ceph-exporter,480,+3
2025-07-11 03:15,coredns,78,+6
2025-07-11 03:15,csi-resizer,2,+0
2025-07-11 03:15,csi-snapshotter,108,+4
2025-07-11 03:15,ddns,10,+0
2025-07-11 03:15,discovery,50,+20
2025-07-11 03:15,filebeat,2286,+103
2025-07-11 03:15,front-app-container,1442,-5
2025-07-11 03:15,fulltext-app-container,6,-388
2025-07-11 03:15,grafana,4,+2
2025-07-11 03:15,istio-proxy,2634,-7
2025-07-11 03:15,kea,89,-4
2025-07-11 03:15,log-collector,110,+57
2025-07-11 03:15,metrics,119,+1
2025-07-11 03:15,mgr,603,+2
2025-07-11 03:15,mon,4592,+146
2025-07-11 03:15,my-redmine,250,+0
2025-07-11 03:15,osd,152,-149
2025-07-11 03:15,paper-app-container,269,+0
2025-07-11 03:15,paper-mongo-container,5,+0
2025-07-11 03:15,powerdns-helm,1,+0
2025-07-11 03:15,prometheus,30,+0
2025-07-11 03:15,stats-app-container,22116,+114
2025-07-11 03:15,stns-server,318,+0
2025-07-11 03:15,vmware-exporter,8455,-5
2025-07-11 03:15,watch-active,234,+3
2025-07-11 03:20,author-app-container,570,+9
2025-07-11 03:20,author-mongo-container,5,+0
2025-07-11 03:20,builder,129,+4
2025-07-11 03:20,cadvisor,2,+0
2025-07-11 03:20,ceph-exporter,476,-4
2025-07-11 03:20,coredns,74,-4
2025-07-11 03:20,csi-snapshotter,108,+0
2025-07-11 03:20,filebeat,2174,-112
2025-07-11 03:20,front-app-container,1442,+0
2025-07-11 03:20,istio-proxy,2637,+3
2025-07-11 03:20,kea,92,+3
2025-07-11 03:20,log-collector,239,+129
2025-07-11 03:20,metrics,120,+1
2025-07-11 03:20,mgr,602,-1
2025-07-11 03:20,mon,4314,-278
2025-07-11 03:20,my-redmine,265,+15
2025-07-11 03:20,osd,483,+331
2025-07-11 03:20,paper-app-container,274,+5
2025-07-11 03:20,paper-mongo-container,6,+1
2025-07-11 03:20,prometheus,30,+0
2025-07-11 03:20,redmine-ticket-receiver,1,+0
2025-07-11 03:20,stats-app-container,22004,-112
2025-07-11 03:20,stns-server,316,-2
2025-07-11 03:20,vmware-exporter,8457,+2
2025-07-11 03:20,watch-active,228,-6
2025-07-11 03:25,author-app-container,230,-340
2025-07-11 03:25,author-mongo-container,2,-3
2025-07-11 03:25,builder,46,-83
2025-07-11 03:25,cadvisor,1,-1
2025-07-11 03:25,ceph-exporter,172,-304
2025-07-11 03:25,coredns,28,-46
2025-07-11 03:25,csi-snapshotter,38,-70
2025-07-11 03:25,discovery,8,-42
2025-07-11 03:25,filebeat,897,-1277
2025-07-11 03:25,front-app-container,483,-959
2025-07-11 03:25,grafana,2,-2
2025-07-11 03:25,istio-proxy,963,-1674
2025-07-11 03:25,jumpsv,5,+0
2025-07-11 03:25,kea,27,-65
2025-07-11 03:25,metrics,44,-76
2025-07-11 03:25,mgr,225,-377
2025-07-11 03:25,mon,2118,-2196
2025-07-11 03:25,my-redmine,96,-169
2025-07-11 03:25,paper-app-container,92,-182
2025-07-11 03:25,paper-mongo-container,2,-4
2025-07-11 03:25,prometheus,11,-19
2025-07-11 03:25,stats-app-container,8170,-13834
2025-07-11 03:25,stns-server,142,-174
2025-07-11 03:25,vmware-exporter,3245,-5212
2025-07-11 03:25,watch-active,84,-144
(venv) c0a22166@c0a22166:~/teian$
```
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
