[Windows インストール チュートリアル](https://github.com/ageitgey/face_recognition/issues/175)
```bash
pip install cmake
pip install dlib
pip install face_recognition
```
.env
顔検出：画像内に人物の顔があるかどうか
顔識別：同一人物と判定できるかどうか
```text
TARGET_EXT=*.jpg（対象となる画像の拡張子）

KNOWN_FOLDER=（判定したい人物を格納するフォルダパス）
UNKNOWN_FOLDER=（判定対象となる画像を格納するフォルダパス）
SORTING_FOLDER=（実行後、判定されて分類された画像を格納するフォルダパス）

UNIDENTIFIED_FOLDER=（顔検出自体ができたい画像の移動先）
THRESHOLD_FOLDER=（下記で顔識別ができなかった画像の移動先）

THRESHOLD=0.45(顔判別をどれだけ厳しくするか。小さいほど厳しくなる。0.0~1.0まで)
```
#### v0.9
以下の使い方を踏襲  
https://github.com/ageitgey/face_recognition#usage
