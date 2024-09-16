import os
from flask import Flask, request, jsonify

from location.data_access import DatabaseAccess

"""
locationモジュール
"""


def create_app() -> Flask:
    ''' Flaskアプリ生成 '''

    from location.modules import db

    """
    位置情報アプリのインスタンス作成
    """
    app = Flask(__name__)

    # SQLiteデータベースの設定
    db_path = get_db_path()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # アプリケーションとSQLAlchemyを初期化
    db.init_app(app)

    # 位置情報登録API エンドポイント
    @app.route('/api/regist_location', methods=['POST'])
    def regist_location():

        try:
            # POSTリクエストで送信されたJSONデータを取得
            data = request.get_json()

            data_access = DatabaseAccess(db)

            # 位置情報を追加
            response, status_code = data_access.add_location(data)

            # 成功時のレスポンス
            return jsonify({"message": "Location registered successfully!"}), 201

        except Exception as e:
            # エラー時のレスポンス
            return jsonify({"error": str(e)}), 400


    # 位置情報表示API エンドポイント
    @app.route('/api/show_location', methods=['POST'])
    def show_location():

        try:
            # POSTリクエストで送信されたJSONデータを取得
            data = request.get_json()

            data_access = DatabaseAccess(db)

            # 成功時のレスポンス
            return jsonify({"message": "Location showed successfully!"}), 201

        except Exception as e:
            # エラー時のレスポンス
            return jsonify({"error": str(e)}), 400

    def get_db_path(name = 'locations.db'):

        # basedir = os.path.abspath(os.path.dirname(__file__))
        # カレントワーキングディレクトリをプロジェクトのベースディレクトリとして設定
        basedir = os.getcwd()

        # データベースを「db」ディレクトリ内に置く
        db_path = os.path.join(basedir, 'db', name)

        # TODO: デプロイ環境では別の場所にしないとね

        return db_path
        
    return app
