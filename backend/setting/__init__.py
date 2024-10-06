from google.cloud import secretmanager


def get_maps_api_key():
    ''' 
    MapAPIのキー値を取得 
    '''
    return get_secret_value_from_gcp('maps_api_key')


def get_secret_value_from_gcp(key):
    '''
    Google Cloud Platform の　Secret Manager から値を取得 
    '''

    client = secretmanager.SecretManagerServiceClient()
    name_value = f"projects/mylocationmonitor-434913/secrets/{key}/versions/latest"
    response = client.access_secret_version(name=name_value)

    return response.payload.data.decode('UTF-8')

'''
Seacret Manaeger の利用方法

1. GCPコンソール > Secret Manager（https://console.cloud.google.com/security/secret-manager）に移動します。
2. 「シークレットを作成」ボタンをクリックし、名前を指定して作成します。この名前がapi_keyの部分に該当します。
'''