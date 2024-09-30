import os
from flask import Flask

from location import create_app
from location.modules import db

# Flaskアプリ生成
app = create_app()

# アプリケーション起動後にcreate_all()を呼び出す
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    # Cloud Run のポート環境変数を使用し、デフォルトは 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
