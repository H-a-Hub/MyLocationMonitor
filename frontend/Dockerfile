# ベースイメージとして Node.js を指定
FROM node:14 AS build

# 作業ディレクトリを作成
WORKDIR /app

# 依存関係ファイルをコピーして依存関係をインストール
COPY package*.json ./
RUN npm install

# ソースコードをコピー
COPY . .

# TypeScript コードをトランスパイルして React アプリをビルド
RUN npm run build

# --------------------------------------------
# 最終的なイメージを作成（軽量な nginx ベース）
FROM nginx:alpine

# ビルド済みのファイルをコピー
COPY --from=build /app/build /usr/share/nginx/html

# デフォルトでポート 80 を公開
EXPOSE 80

# Nginx を起動
CMD ["nginx", "-g", "daemon off;"]
