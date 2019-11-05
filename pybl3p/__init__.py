import requests
import websockets

__version__ = '0.1.0'


def http_request(
        callname: str,
        url='https://api.bl3p.eu',
        api_version=1,
        market='BTCEUR'
):
    path = f'/{api_version}/{market}/{callname}'

    response = requests.request(
        method='POST',
        url='{}{}'.format(url, path),
        timeout=(5, 10),
        allow_redirects=False,
        verify=True,
    )
    if response.status_code != 200:
        raise Exception('unexpected response code: %d' % response.status_code)

    return response.json()


async def websocket_request(
        channel: str = 'orderbook',
        url: str = 'wss://api.bl3p.eu',
        version: int = 1,
        market: str = 'BTCEURO'
):
    """
    args:

    note: server seems to always give a 400, not sure why yet.
    """
    uri = f"{url}/{version}/{market}/{channel}/"
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            print(f"{message}")
