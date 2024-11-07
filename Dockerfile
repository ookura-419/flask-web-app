# ベースイメージとしてPythonの公式軽量イメージを使用
FROM python:3.9-slim

# コンテナ内の作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt requirements.txt

# 必要なPythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをすべてコピー
COPY . .

# アプリケーションを起動するコマンドを指定
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
