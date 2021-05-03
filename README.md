# amazon-lib-list

kindle for mac が生成するKindleSyncMetadataCache.xmlをパースしてASINリストを作成する

参考：[Kindle蔵書一覧を取得する方法 - Qiita コメント](https://qiita.com/taka_hira/items/8a9181c0733de2c9f8ee#comment-55d0067c26a2fcbaa184)

```bash
% docker-compose build amazon-lib-list
```

```bash
% mkdir work
% cp ${HOME}/Library/Containers/com.amazon.Kindle/Data/Library/Application\ Support/Kindle/Cache/KindleSyncMetadataCache.xml work/KindleSyncMetadataCache.xml
```

```bash
% sh run.sh
```

入出力ファイルを変更する場合には settigs.json を編集
