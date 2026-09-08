# Discord Bot

Python製のDiscord Botをクラウド環境で常時動かすための最低限の機能のみのサンプルです．

Dockerfileを利用できるホスティングサービスでの稼働を想定しており，Koyeb,Northflankで動作確認済みです．

## 環境
- Python
- discord.py
- Flask
- Dockerfileが利用できるホスティングサービス

## 特徴
- discord.pyを利用したDiscord Bot
- `!ヌルポ`→`ガッ`というコマンド
- FlaskによるHTTPエンドポイントを提供
- Dockerによる実行環境の構築
- 環境変数によってローカル/クラウド環境の切り替え可能
- Botのトークンをコードに直接記述せず，環境変数として管理

## ディレクトリ
```
.
├── app/                # BotのPythonファイルをまとめるディレクトリ
│ ├── main.py           # Bot本体
│ └── web_server.py     # FlaskによるWebサーバ
├── Dockerfile          # Dockerイメージの構築設定
├── requirements.txt    # 必要なPythonライブラリ
├── .env.example        # ローカルで使用する`.env`のサンプル
├── .gitignore          # Gitの追跡対象から除外するファイルを指定
├── LICENSE             # ライセンス
└── README.md           # このファイル
```

## 環境変数
ローカル環境で開発する際には，`.env.example`をコピーして，`.env`ファイルを作成してください

### BOT_TOKEN
Discord Developer Portalで取得したBot Tokenを設定してください．
Bot Tokenは秘密情報のため，GitHub，クラウド環境などに公開しないよう注意してください．

### LOCAL_MODE
`false`の場合，FlaskのHTTPサーバを起動します．
ローカルで実行する場合には`true`に設定してください．
ローカル環境でBotをテストするなどに利用できます．
デフォルトの設定は`false`なので，クラウド環境では，設定しない場合は`false`として動作します．

## ローカルの環境構築
必要なライブラリをインストールしてください．
```
pip install -r requirements.txt
```
Botを起動します．
```
python app/main.py
```
Botが参加しているサーバで
```
!ヌルポ
```
と送信すると
```
ガッ
```
と返信されれば，正常に動作しています．

## クラウド環境での利用
プロジェクトをGitHubにアップロードして，各ホスティングサービスで，リポジトリをリンクさせることで利用できます．
ホスティングサービスで，シークレット環境変数にBot Tokenを設定することで，Botをクラウドで運用できます．
間違っても，通常の環境変数にBot Tokenを登録して公開しないよう注意してください！！