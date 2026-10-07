# AI Learning — Chapter I · Part 1: Construction and Learning Principles of Neural Networks

中高生から始められる、無料の日本語教材です。数式を暗記する前に、入力・重み・予測・誤差・学習を自分で動かします。

## はじめる

1. [ブラウザ教材を開く](https://so10102020.github.io/ai-neural-network-course/)（インストール不要）
2. 第1節から順番に進み、各節の「検討課題」に答える
3. 第4節まで終えたら、下の Python 演習に挑戦する

ブラウザ教材は [docs/index.html](docs/index.html) にあります。GitHub Pages が未反映の場合は、ファイルをブラウザで開いても使えます。

## 学習の道筋

| Section | Topic | 到達目標 |
| --- | --- | --- |
| 1 | Basic Structure | 入力から予測までの流れを説明できる |
| 2 | Single Neuron | 重み・バイアス・活性化関数を操作できる |
| 3 | Parameter Training | 損失と更新の関係を説明できる |
| 4 | Multilayer Structure & XOR | 隠れ層が必要な例を説明できる |
| 5 | Model Evaluation | 訓練用とテスト用を分け、失敗を調べられる |

目安は各節20〜40分。中学数学の四則演算があれば第3節まで進められます。第4節以降の式や Python は、高校数学を学びながらでも大丈夫です。

## Python 演習

Python 3.9 以上を使います。追加ライブラリは不要です。

```bash
python3 exercises/01_neuron.py
python3 exercises/02_train.py
python3 exercises/03_xor.py
```

- `01_neuron.py`：重みとバイアスを変え、予測がどう変わるか観察する
- `02_train.py`：勾配を使って1個のニューロンを学習させる
- `03_xor.py`：1層では解けない XOR を、隠れ層のあるネットワークで学ぶ

各ファイルの先頭に課題があります。出力の数値を写すだけでなく、「変更前後で何が変わったか」を言葉で説明してください。解説は [演習ガイド](exercises/GUIDE.md) にあります。

## この教材の約束

- 「ニューロン」は脳から着想を得た計算の部品です。人間の脳をそのまま再現したものではありません。
- 小さな例で動いても、現実の画像や文章で同じ性能が出るとは限りません。
- 正解率だけでなく、どの入力で間違えたかを確認します。
- 教材の説明や誤りは [Issues](https://github.com/so10102020/ai-neural-network-course/issues) で報告できます。

## ライセンス

教材本文と図・画面は [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)、サンプルコードは [MIT License](LICENSE-CODE) です。出典を示せば授業や自習で再利用できます。
