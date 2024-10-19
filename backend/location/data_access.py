from flask import jsonify
# from flask_sqlalchemy import SQLAlchemy

from .modules import Location

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
            location, status = self.create_location(data)

            # データベースに追加してコミット
            self.add(location)
            self.commit()
            
        except Exception as e:
            self.rollback()    # エラー時はロールバックしておく
            raise e


    def create_location(self, data):
        """
        Locationオブジェクトを生成
        """

        user = data.get('user')
        timestamp = data.get('timestamp')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if user is None or latitude is None or longitude is None or timestamp is None:
            raise Exception(f'data has none elements {data}')

        return Location(user=user, latitude=latitude, longitude=longitude, timestamp=timestamp), 200

    def get_last_location(self):
        """
        最新の緯度と経度の位置情報をデータベースから取得するメソッド
        """
        try:
            # Locationモデルをタイムスタンプで降順にソートし、最初のレコードを取得
            last_location = self.query(Location).order_by(Location.timestamp.desc()).first()

            # レコードが存在しない場合
            if last_location is None:
                raise Exception("No location data available")

            return last_location
            
        except Exception as e:
            raise e