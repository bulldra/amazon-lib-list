# amazon-lib-list

kindle for mac が生成するKindleSyncMetadataCache.xmlをパースしてASINリストを作成する

参考：[Kindle蔵書一覧を取得する方法 - Qiita コメント](https://qiita.com/taka_hira/items/8a9181c0733de2c9f8ee#comment-55d0067c26a2fcbaa184)

## build

```bash
% docker-compose build amazon-lib-list
```

## run

```bash
% sh run.sh
```

KindleSyncMetadataCache.xml を work にコピーして蔵書一覧に変換  
入出力ファイルを変更する場合には settigs.json を編集
