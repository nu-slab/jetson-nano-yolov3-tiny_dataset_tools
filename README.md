# FPGA デザインコンテスト 物体認識
- YOLOの学習用データセットを作る際のツール群です。

|Name|Explanation|
|:-------------|:---|
|[classify](./classify) |画像やラベルのファイルをtrain用・valid用・test用に分割します。|
|[preview_dataset](./preview_dataset)           |学習データセットのBBoxを画像上に表示します。|
|[rename_file](./rename_file)|画像やラベルのファイルを一括で置換します。|
|[resize_img](./resize_img)|画像やラベルを指定の画像サイズに変換します。|
|[resize_only_img](./resize_only_img)|画像のみを指定の画像サイズに変換します。|
|[merge_dataset](./merge_dataset)|2つのデータセットをマージします。|
|[OIDv6_format_to_yolo_format](./OIDv6_format_to_yolo_format)|OIDv6で取得したデータセットをYOLO形式に変換します。|
|[rm_img_GUI](https://github.com/yarakigit/rm_img_GUI)|データセットに相応しくない画像をGUIで削除|
|[select_dataset](./select_dataset)|学習データセットから一部抜粋|
|[sandbox](./sandbox)|その他のツール|
