# 概要
- 画像のみを指定の画像サイズに変換します。(画像のwidthとheightは同じ)

# 実行
~~~bash
$ make
~~~
- 引数
  - ```IN_DIR``` : オリジナルのディレクトリ
  - ```IMG_TYPE``` : 画像の拡張子
  - ```RESIZI_SIZE``` :  リサイズされるwidthとheightの大きさ (YOLOのデフォルトは416)
- [/output](./output)に結果が格納されます。