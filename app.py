from flask import request, jsonify

from location import create_app
from location.modules import db


#--------------------------

# Flaskアプリ生成
app = create_app()

# アプリケーション起動後にcreate_all()を呼び出す
with app.app_context():
    db.create_all()

#--------------------------

# アプリケーションのエントリーポイント
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
