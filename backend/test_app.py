import unittest

from .location import create_app
from .location.modules import db


class WebApiTest(unittest.TestCase):
    """
    WebAPIのテスト
    """

    def setUp(self):
        """テストのセットアップ"""
        self.app = create_app()  # アプリを取得
        self.app.testing = True  # テストモードを有効化
        self.client = self.app.test_client()  # テストクライアントを作成
        with self.app.app_context():
            db.create_all()  # テスト用データベースを初期化

    def tearDown(self):
        """テスト終了後のクリーンアップ"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()  # テスト終了後にデータベースを削除

    def test_regist_location_success(self):
        # 正しいデータを使ってPOSTリクエストを送信
        payload = {
            "user": "taro",
            "timestamp": "2024/09/16 12:22:54.800",
            "latitude": 35.6895,
            "longitude": 139.6917
        }
        response = self.client.post('/api/regist_location', json=payload)
        
        # ステータスコードが201（Created）であることを確認
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Location registered successfully!', response.data)

    def test_regist_location_missing_data(self):
        # 緯度が不足している不正なデータを使ってPOSTリクエストを送信
        payload = {
            "longitude": 139.6917
        }
        response = self.client.post('/api/regist_location', json=payload)

        # ステータスコードが400（Bad Request）であることを確認
        self.assertEqual(response.status_code, 400)

    def test_regist_location_invalid_data(self):
        # 不正な形式のデータを使ってPOSTリクエストを送信
        payload = {
            "user": "jiro",
            "timestamp": "2024/12/11 0:0:0",
            "latitude": "invalid",  # 無効な値
            "longitude": 139.6917
        }
        response = self.client.post('/api/regist_location', json=payload)

        # ステータスコードが400であることを確認
        self.assertEqual(response.status_code, 400)

    def test_show_location(self):
        # 位置情報表示APIテスト
        payload = {
            "latitude": 35.6895,
            "longitude": 139.6917
        }
        response = self.client.post('/api/show_location', json=payload)
        
        # ステータスコードが200であることを確認
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
