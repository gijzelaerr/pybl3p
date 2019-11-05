import requests
from os import environ
from time import time
from urllib.parse import urlencode
import hmac
import base64
import hashlib


def make_headers(params: dict, path: str) -> dict:
    pub_key = environ['BL3P_PUB']
    priv_key = environ['BL3P_PRIV']

    params['nonce'] = str(int(time() * 1000000))
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


def http_request(
        callname: str,
        url='https://api.bl3p.eu',
        api_version=1,
        market='BTCEUR',
        namespace: str = 'money',
        params=None,
):
    """
    args:
        callname: Name of call (for example: “wallet/history”)
        api_version: Version of API (is currently: 1)
        market: Market that the call will be applied to., one of BTCEUR, LTCEUR, GENMKT
        namespace: Namespace of call. Usually: "money"

    Note:
        GENMKT is used for market independent calls
    """
    assert market in ('BTCEUR', 'LTCEUR', 'GENMKT')

    if not params:
        params = {}

    path = f"/{api_version}/{market}/{namespace}/{callname}"

    headers = make_headers(params, path)


    response = requests.request(
        method='POST',
        url='{}{}'.format(url, path),
        data=params,
        headers=headers,
        timeout=(5, 10),
        allow_redirects=False,
        verify=True,
    )

    if response.status_code != 200:
        raise Exception('unexpected response code: %d' % response.status_code)

    return response.json()


def order_add():
    """
    Create an order
    """
    raise NotImplemented


def order_cancel():
    """
    Cancel an order
    """
    raise NotImplemented


def order_result():
    """
    Get a specific order
    """
    raise NotImplemented


def order_full():
    """
    Get the whole orderbook
    """
    raise NotImplemented


def wallet_history(currency: str = 'EUR', page: int = 1):
    """
    get the transaction history

    args:
        currency: Currency of the wallet. (Can be: 'BTC', 'EUR')
        page: Page number. (1 = most recent transactions)

    """
    params = {'currency': currency, 'page': page}
    return http_request(callname='wallet/history', market='GENMKT', params=params)


def new_deposit_address():
    """
     Create a new deposit address
    """
    raise NotImplemented


def deposit_address():
    """
    Get the last deposit address
    """
    raise NotImplemented


def withdraw():
    """
    Create a withdrawal
    """
    raise NotImplemented


def info():
    """
    Get account info & balance
    """
    raise NotImplemented


def orders():
    """
    Get active orders
    """
    raise NotImplemented


def orders_history():
    """
    Get order history
    """
    raise NotImplemented


def trades_fetch():
    """
    Fetch all trades on BL3P
    """
    raise NotImplemented
