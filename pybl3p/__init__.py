import requests
from typing import List, Tuple

__version__ = '0.1.0'


def _request(callname, url='https://api.bl3p.eu', api_version=1, market='BTCEUR'):
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


def trades():
    """
    Last 1000 trades

    :return: Array of trades.
    """
    return _request('trades')


def tradehistory(timefactor: str = None, timevalue: int = None) -> List[Tuple[int, float, float]]:
    """
     Trade history

    :return: tradehistory, An array containing datapoints

    The 'tradehistory' array will contain:
        The time of the datapoint (long)
        The price of the datapoint (float)
        The volume of the datapoint (float)


    """
    assert((timefactor is None) == (timevalue is None))

    if timefactor:
        assert(timefactor in ('h', 'd', 'm', 'y'))

    return _request('trades')
