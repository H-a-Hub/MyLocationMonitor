from flask_sqlalchemy import SQLAlchemy

from location.modules import Location


class DatabaseAccess:
    """ データベースアクセスを提供するクラス """
    
    def __init__(self, db: SQLAlchemy):
        """ コンストラクタ: SQLAlchemyのインスタンスを受け取り、データベースを初期化する """
        self._db = db  # インスタンス変数としてdbを初期化

    def add(self, instance):
        """ レコードを追加するメソッド """
        self._db.session.add(instance)

    def commit(self):
        """ コミットするメソッド """
        self._db.session.commit()

    def query(self, model):
        """ モデルに基づいてクエリを実行するメソッド """
        return self._db.session.query(model)
    
    def remove(self, instance):
        """ レコードを削除するメソッド """
        self._db.session.delete(instance)

    def rollback(self):
        """ ロールバックするメソッド """
        self._db.session.rollback()

    def add_location(self, data):
        """
        緯度と経度の位置情報をデータベースに保存するメソッド
        """
        try:
            location = create_location(data)

            # データベースに追加してコミット
            self.add(location)
            self.commit()

            return {"message": "Location registered successfully!"}, 201
            
        except Exception as e:
            # エラー時はロールバックしてエラーメッセージを返す
            self.rollback()
            return {"error": str(e)}, 400

    def create_location(data) -> Location:
        """
        Locationオブジェクトを生成
        """

        user = data.get('user')
        timestamp = data.get('timestamp')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None or timestamp is None:
            return jsonify({"error": "Latitude and longitude are required"}), 400

        return Location(user=user, latitude=latitude, longitude=longitude, timestamp=timestamp)
