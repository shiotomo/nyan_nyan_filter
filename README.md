# にゃんにゃんフィルター

## にゃんにゃんフィルターとは

社会性フィルターみたいなもの。
予めテキストファイルにNGワードを登録しておき、誤って自分がそれに関するツイートをしてしまった場合、そのツイートを即座に削除し、代わりに「にゃんにゃんフィルター発動」とつぶやくサーバーアプリ。

## 使用ツール

- python3
- tweepy

## 環境構築

tweepyのインストール
```
pip install tweepy
```

dictionary.txtといった名前のファイルを作成し、中に、NGワードを書いていく。  

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
  
  - ストリーミングによりNGワードを監視します
 
- clientモード
  
  - 開発中
  
- update tokenモード
  
  - APIキーを更新するときに使うモードです。
 
 
