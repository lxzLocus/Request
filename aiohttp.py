import aiohttp
import asyncio

async def request():
    endpoint = '/'
    url = f'http://{endpoint}'

    payload = {
        # ペイロードデータをここに記載
    }

    headers = {
        'Content-Type': 'application/json'
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload, headers=headers) as response:
                response_data = await response.json()  # レスポンスがJSON形式の場合
                print(response_data)
        except aiohttp.ClientError as error:
            print(f"Error: {error}")

# 非同期関数を実行するためのエントリーポイント
if __name__ == '__main__':
    asyncio.run(request())
