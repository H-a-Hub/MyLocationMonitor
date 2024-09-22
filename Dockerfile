# Pythonイメージをベースにする
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 空のサブディレクトリを作成
RUN mkdir -p /app/db /app/tmp /app/log

# ソースファイルをコピー
COPY app.py app.py
COPY location/*.py /app/location/

# 依存関係をインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Flaskの起動時に使うポートを指定
ENV PORT 8080

# ポート8080を公開
EXPOSE 8080

# アプリケーションを起動
CMD ["python", "app.py"]
