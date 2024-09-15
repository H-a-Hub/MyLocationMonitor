from flask_sqlalchemy import SQLAlchemy

# SQLAlchemyインスタンスをグローバルに定義
db = SQLAlchemy()


# 位置情報テーブルのモデル
class Location(db.Model):
    
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)    # インデント
    user = db.Column(db.String, nullable=True)         # ユーザー名
    latitude = db.Column(db.Float, nullable=False)  # 経度
    longitude = db.Column(db.Float, nullable=False) # 緯度
    created_at = db.Column(db.DateTime, default=db.func.now())  # レコード作成時のタイムスタンプ
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())  # レコード更新時のタイムスタンプ

