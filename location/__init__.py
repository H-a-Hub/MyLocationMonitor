import os
from flask import Flask, request, jsonify

from location.data_access import DatabaseAccess

from map import get_google_map_data

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

    @app.route('/')
    def hello():
        return 'My Location Monitor.'

    # 位置情報登録API エンドポイント
    @app.route('/api/regist_location', methods=['POST'])
    def regist_location():

        try:
            # POSTリクエストで送信されたJSONデータを取得
            data = request.get_json()

            # 位置情報を追加
            DatabaseAccess(db).add_location(data)

            # 成功時のレスポンス
            return jsonify({"response": "Location registered successfully!"}), 201

        except Exception as e:
            # エラー時のレスポンス
            return jsonify({"error": str(e)}), 400


    # 位置情報全削除API エンドポイント
    @app.route('/api/rm_data', methods=['POST'])
    def rm_data():

        try:
            # POSTリクエストで送信されたJSONデータを取得
            data = request.get_json()

            # db を削除


            # 成功時のレスポンス
            return jsonify({"response": "Location registered successfully!"}), 201

        except Exception as e:
            # エラー時のレスポンス
            return jsonify({"error": str(e)}), 400


    # 位置情報表示API エンドポイント
    @app.route('/api/show_location', methods=['POST'])
    def show_location():

        try:
            # POSTリクエストで送信されたJSONデータを取得
            data = request.get_json()

            latitude = data.get('latitude')
            longitude = data.get('longitude')

            res = get_google_map_data(latitude, longitude)

            # 成功時のレスポンス
            return res, 200

        except Exception as e:
            # エラー時のレスポンス
            return jsonify({"error": str(e)}), 400

    return app


def get_db_path(name = 'locations.db'):

    # basedir = os.path.abspath(os.path.dirname(__file__))
    # カレントワーキングディレクトリをプロジェクトのベースディレクトリとして設定
    basedir = os.getcwd()

    # データベースを「db」ディレクトリ内に置く
    db_path = os.path.join(basedir, 'db', name)

    # TODO: デプロイ環境では別の場所にしないとね

    return db_path
