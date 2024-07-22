import requests

def request():
    endpoint = '/'
    url = f'http://{endpoint}'

    payload = {
        # ペイロードデータをここに記載
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(response.json())  # レスポンスがJSON形式の場合
    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")

request()
