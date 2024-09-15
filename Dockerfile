# Pythonイメージをベースにする
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
COPY app.py app.py

# 依存関係をインストール
RUN pip install -r requirements.txt

# ポートを設定
EXPOSE 8080

# アプリケーションを起動
CMD ["python", "app.py"]
