import unittest

from .location import create_app
from .location.modules import db


# ユニットテスト環境構築手順 
# ディレクトリ移動
#  cd backend/
# Python仮想環境構築
#  python3 -m venv venv
# 仮想環境有効か
#  source venv/bin/activate
# Flask等をインストール
#  pip install -r requirements.txt
#   → backend/venv ディレクトリにインストールされます
# 仮想環境を無効化したい場合は、deactivate


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

    def test_get_last_location(self):
        # モックのセットアップ
        mock_location = MagicMock()
        mock_location.user = "test_user"
        mock_location.latitude = 35.6895
        mock_location.longitude = 139.6917
        mock_location.timestamp = "2024-10-18T15:30:00Z"

        # DatabaseAccessのget_last_locationメソッドをモック
        with unittest.mock.patch.object(DatabaseAccess, 'get_last_location', return_value=mock_location):
            response = self.client.get('/api/get_last_location')

            # ステータスコードが200であることを確認
            assert response.status_code == 200

            # レスポンスのJSONデータを取得
            data = response.get_json()

            # JSONデータが期待通りであることを確認
            assert data['response']['user'] == "test_user"
            assert data['response']['latitude'] == 35.6895
            assert data['response']['longitude'] == 139.6917
            assert data['response']['timestamp'] == "2024-10-18T15:30:00Z"

    def test_get_last_location_no_data(self):
        # DatabaseAccessのget_last_locationメソッドが例外をスローするようにモック
        with unittest.mock.patch.object(DatabaseAccess, 'get_last_location', side_effect=Exception("No location data available")):
            response = self.client.get('/api/get_last_location')

            # ステータスコードが400であることを確認
            assert response.status_code == 400

            # エラーメッセージが正しいかを確認
            data = response.get_json()
            assert data['error'] == "No location data available"

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
