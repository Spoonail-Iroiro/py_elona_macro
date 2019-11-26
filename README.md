elonaマクロ（python版）
====

pyautoguiとついでにtesseract（tesserocr使用）でelonaマクロ
ほぼ自分用

## 環境
Anaconda 4.7.12
python3.7.0
pyautogui
pillow
PySide2
tesserocr

py_macro.ymlにも記載

## 使い方
- area_setting_guiを起動、マウスドラッグでOCR監視範囲を指定
- elonaのEEx使用でログウィンドウを指定すること  フォントサイズを大きくすると読み取り精度が上がって安定
- tesser_macro.pyを実行するとマクロ開始
- 何のマクロを実行するかは"from XXXXX import main"の部分書き換えて指定 マクロスクリプトはmacroフォルダ内にある
+ elona_all_harvest…収穫の魔法書読み切り 1マスだけ残したシェルターで実行 ショートカットは6が魔法書7が詠唱3がふかパンuが休憩
+ elona_harvest…収穫の魔法書願いの杖厳選 縦方向に2マス残した牧場で下のマスに立って実行 ショートカットは上と同じ
+ elona_fukapan…ふかパン作成　2がテスト用ナベ3がふかパン　途中金貨がある選択肢（[a]等）の指定は都度書き換えること

## ライセンス
MIT

## 作者
[Spoonail](https://twitter.com/Spoonail)
