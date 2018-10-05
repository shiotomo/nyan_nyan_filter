# にゃんにゃんフィルター

## 注意

このアプリケーションはTwitterAPIの仕様が変更したため、現在は利用することができません。

## にゃんにゃんフィルターとは

Twitter用社会性フィルターみたいなものです。
予めテキストファイルにNGワードを登録しておき、誤って自分がそれに関するツイートをしてしまった場合、そのツイートを即座に削除し、代わりに「にゃんにゃんフィルター発動」とつぶやくサーバアプリケーションです。

## 使用ツール

- python3
- tweepy

## 環境構築

tweepyのインストール
```
pip install tweepy
```

dictionary.txtといった名前のファイルを作成し、中に、NGワードを書いていきます。  

実行する前に、src/stream.pyの中を変更してください。

実行
```
python3 main.py
```

## 構成

```
main.py
dictionary.txt
README.md
json
  |
  |----- token.json
 
src
  |
  |--- filter.py
  |--- mode.py
  |--- reader.py
  |--- recorder.py
  |--- stream.py
  |--- token.py
```

## モード

- serverモード
  - ストリーミングによりNGワードを監視します。
 
- update tokenモード
  - APIキーを更新するときに使うモードです。
 
 
