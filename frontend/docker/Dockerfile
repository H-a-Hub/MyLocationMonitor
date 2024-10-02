# WordPressとTypeScriptのビルド環境をセットアップ

# Stage 1: Node.js環境でTypeScriptのビルド
FROM node:16 AS build

# 作業ディレクトリの設定
WORKDIR /app

# パッケージファイルをコピーして依存関係をインストール
COPY wp-content/themes/map-theme/package*.json ./wp-content/themes/map-theme/
RUN cd wp-content/themes/map-theme && npm install

# ソースコードをコピー
COPY wp-content/themes/map-theme/ ./wp-content/themes/map-theme/

# TypeScriptのビルドを実行
RUN cd wp-content/themes/map-theme && npm run build

# Stage 2: PHPとApacheをベースにWordPressをセットアップ
FROM wordpress:php7.4-apache

# 作業ディレクトリの設定
WORKDIR /var/www/html

# WordPressコンテンツのディレクトリをコピー
COPY wp-content /var/www/html/wp-content

# ファイルの権限設定
RUN chown -R www-data:www-data /var/www/html/wp-content

# ポートの設定
EXPOSE 80
