import requests

from ..setting import get_maps_api_key

def request_google_map_data(latitude, longitude):
    ''' 
    Google Map のデータをリクエスト 
    '''

    api_key = get_maps_api_key()

    # Google Maps APIのリクエストURL
    google_maps_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=1500&type=restaurant&key={api_key}'

    # Google Maps APIへのリクエスト
    response = requests.get(google_maps_url)

    return response

'''
APIキーについて

「APIの制限」項目で、以下を有効にしてください
Places API
'''