import base64
import hashlib
import hmac
from os import environ
import json
from time import time
from urllib.parse import urlencode

import requests
import websockets


def do_request(
        url: str,
        params: dict = None,
        headers: dict = None
):
    response = requests.request(
        method='POST',
        url=url,
        timeout=(5, 10),
        allow_redirects=False,
        verify=True,
        data=params,
        headers=headers,
    )
    if response.status_code != 200:
        raise Exception('unexpected response code: %d' % response.status_code)

    parsed = response.json()
    return parsed


def public_request(
        callname: str,
        base_url: str = 'https://api.bl3p.eu/1/',
        market: str = 'BTCEUR',
        params: dict = None,
):
    assert market in ('BTCEUR', 'LTCEUR', 'GENMKT')

    if not params:
        params = {}

    path = f'{market}/{callname}'
    url = f"{base_url}{path}"
    return do_request(url, params)


async def websocket_request(
        channel: str = 'trades',
        base_url: str = "wss://api.bl3p.eu/1",
        market: str = 'BTCEUR'
):
    """
    args:
        channel: trades or orderbook
    note: server seems to always give a 400, not sure why yet.
    """
    assert (channel in ('trades', 'orderbook'))
    url = f"{base_url}/{market}/{channel}"
    async with websockets.connect(url) as websocket:
        async for message in websocket:
            yield json.loads(message)


def private_request(
        callname: str,
        url_base='https://api.bl3p.eu/1/',
        market='BTCEUR',
        namespace: str = 'money',
        params=None,
):
    """
    args:
        callname: Name of call (for example: “wallet/history”)
        market: Market that the call will be applied to., one of BTCEUR, LTCEUR, GENMKT
        namespace: Namespace of call. Usually: "money"

    Note:
        GENMKT is used for market independent calls
    """
    assert market in ('BTCEUR', 'LTCEUR', 'GENMKT')

    if not params:
        params = {}

    params['nonce'] = str(int(time() * 1000000))

    path = f"{market}/{namespace}/{callname}"
    headers = make_headers(params, path)
    url = f"{url_base}{path}"
    response = requests.request(
        method='POST',
        url=url,
        data=params,
        headers=headers,
        timeout=(5, 10),
        allow_redirects=False,
        verify=True,
    )

    if response.status_code != 200:
        raise Exception('unexpected response code: %d' % response.status_code)

    return response.json()


def make_headers(params: dict, path: str, pub_key: str = None, priv_key: str = None) -> dict:
    """
    Create the headers for a private request

    args:
        params: A dict of request parameters
        path: The request path
        pub_key: Your bl3p public key. If not set the `BL3P_PUB` environment variable is used.
        priv_key: Your bl3p private key.  If not set the `BL3P_PRIV` environment variable is used.

    """
    if not pub_key:
        pub_key = environ['BL3P_PUB']

    if not priv_key:
        priv_key = environ['BL3P_PRIV']

    encoded_payload = urlencode(params)
    message = '{:s}{:c}{:s}'.format(path, 0x00, encoded_payload)

    signature = hmac.new(
        key=base64.b64decode(priv_key),
        msg=message.encode(),
        digestmod=hashlib.sha512
    ).digest()

    headers = {
        'Rest-Key': pub_key,
        'Rest-Sign': base64.b64encode(signature).decode(),
    }

    return headers
