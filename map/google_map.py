import requests



def get_google_map_data(lat, lng):

    api_key = get_api_key()

    # Google Maps APIのリクエストURL
    google_maps_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=1500&type=restaurant&key={api_key}'

    # Google Maps APIへのリクエスト
    response = requests.get(google_maps_url)

    # エラーチェック
    if response.status_code != 200:
        return jsonify({'error': 'Failed to connect to Google Maps API'}), 500

    # レスポンスデータを返却
    return jsonify(response.json())


def get_api_key():

    # JSONファイルのパス
    config_path = 'res/config.json'

    # ファイルを開いて内容を読み込む
    with open(config_path, 'r') as config_file:
        config_data = json.load(config_file)

    # "api_key"の値を取得
    return config_data.get('api_key')
