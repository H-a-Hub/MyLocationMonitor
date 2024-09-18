# Pythonイメージをベースにする
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
COPY app.py app.py

# 依存関係をインストール
RUN pip install -r requirements.txt

# Flaskの起動時に使うポートを指定
ENV PORT 8080

# ポート8080を公開
EXPOSE 8080

# アプリケーションを起動
CMD ["python", "app.py"]
