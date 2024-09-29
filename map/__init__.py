import requests

from env import get_maps_api_key

def get_google_map_data(latitude, longitude):
    ''' 
    Google Map のデータを取得 
    '''

    api_key = get_maps_api_key()

    # Google Maps APIのリクエストURL
    google_maps_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=1500&type=restaurant&key={api_key}'

    # Google Maps APIへのリクエスト
    response = requests.get(google_maps_url)

    # エラーチェック
    if response.status_code != 200:
        return jsonify({'error': 'Failed to connect to Google Maps API'}), 500

    # レスポンスデータを返却
    return jsonify(response.json())

