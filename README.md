[Windows インストール チュートリアル](https://github.com/ageitgey/face_recognition/issues/175) を参考にしながらFace Recognitionによる人物画像の分類を行うためのプログラム  

## 事前準備
```bash
pip install cmake
pip install dlib
pip install face_recognition
```
* .envに格納フォルダ、出力フォルダを設定  
  * 顔認識：画像内に人物の顔があるかどうか  
  * 顔認証：同一人物と判定できるかどうか
  * （KNOWN_UNIDENTIFIED_FOLDERの意味は下部の所感で説明）
```text
TARGET_EXT=*.jpg（対象となる画像の拡張子）

UNKNOWN_FOLDER=（判定対象となる画像を格納するフォルダパス）
SORTED_FOLDER=（分類された画像を格納するフォルダパス。実行後、顔認証された画像が追加されていく）

KNOWN_UNIDENTIFIED_FOLDER=（手動で分類したが、顔認識ができない画像の移動先）
UNIDENTIFIED_FOLDER=（顔認識自体ができたい画像の移動先）
THRESHOLD_FOLDER=（下記で顔認証ができなかった画像の移動先）

THRESHOLD=0.45(顔判別をどれだけ厳しくするか。小さいほど厳しくなる。0.0~1.0まで)
```
### 起動
```
python main.py
```
### 実行結果
```
移動前ファイル数: 0
cannot find faces in: D:\Python\images\BarackObama-1531259328346333184-20220530_220047-img1.jpg
cannot find faces in: D:\Python\images\BarackObama-1540340648972279813-20220624_232643-img1.jpg
cannot find faces in: D:\Python\images\BarackObama-1541949895296311297-20220629_100117-img1.jpg
ok JoeBiden : D:\Python\images\POTUS-1565834643609456640-20220903_075045-img1.jpg
out of threshold: D:\Python\images\POTUS-1565867419553468416-20220903_100059-img1.jpg
out of threshold: D:\Python\images\POTUS-1566922883934441473-20220906_075502-img1.jpg
out of threshold: D:\Python\images\POTUS-1567236715064041479-20220907_044205-img1.jpg
ok JoeBiden : D:\Python\images\POTUS-1567515201855004674-20220907_230841-img1.jpg
out of threshold: D:\Python\images\POTUS-1567586398504370179-20220908_035136-img1.jpg
out of threshold: D:\Python\images\POTUS-1567586398504370179-20220908_035136-img2.jpg
ok BarackObama : D:\Python\images\POTUS-1567640240533168130-20220908_072533-img1.jpg
out of threshold: D:\Python\images\POTUS-1568343500298797057-20220910_060003-img1.jpg
out of threshold: D:\Python\images\POTUS-1568631646932312064-20220911_010503-img1.jpg
...（略）
移動後ファイル数: 58
```

## 所感
* 人物の顔を検出するための顔認識自体の精度がいまひとつ
  * 検出が難しいマスクありの顔、横顔に加え、ピースなどで指が顔に被っている、画像サイズに対して顔が小さい、逆に大きすぎる、顔の一部しか映っていない等の状況によっても検出できないことが多い
  * そのため、判別済の画像を参照する際も顔認識ができないことがあるため、一旦画像を退避しておくための格納フォルダ先を用意した（KNOWN_UNIDENTIFIED_FOLDER）
* 検出後に同一人物かどうかを判定する顔認証については、閾値を0.5ほどにするとまずまず。正答率は7割程度

## バージョン
#### v0.9
以下の使い方を踏襲  
https://github.com/ageitgey/face_recognition#usage

#### v1.0
実行回数を重ねるほど、遅くはなるが精度を上げるため分類後の画像を都度参照するようにする  

0. 先にいくつかの画像をsortedフォルダに入れておく
1. sortedフォルダを学習対象として、unkwownフォルダの画像を組み分けていく
