from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
'''
SQLAlchemyインスタンス
'''

class Location(db.Model):
    ''' 位置情報テーブルのモデル '''
    
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)    # インデント
    user = db.Column(db.String, nullable=True)      # ユーザー名
    latitude = db.Column(db.Float, nullable=False)  # 経度
    longitude = db.Column(db.Float, nullable=False) # 緯度
    timestamp = db.Column(db.String, nullable=False) # タイムスタンプ

