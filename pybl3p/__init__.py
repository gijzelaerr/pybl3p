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


def ticker() -> (str, float, float, float, Tuple[float, float]):
    """

    Returns:
        a tuple containing:

            currency: The currency the returned values apply to
            last: Price of the last trade
            bid: Price of the current bid
            ask: Price of the current ask
            volume: tuple of trades executed for the regarding order:

                24h: Volume of the last 24 hours
                30d: Volume of the last 30 days
    """
    return _request('ticker')


def trades():
    """
    Last 1000 trades

    Returns:
         A list of trades.
    """
    return _request('trades')


def tradehistory(timefactor: str = None, timevalue: int = None) -> List[Tuple[int, float, float]]:
    """
    Trade history

    Returns:
        A list of datapoint tuples containing:

            time:  The time of the datapoint
            price: The price of the datapoint
            volume: The volume of the datapoint
    """
    assert((timefactor is None) == (timevalue is None))

    if timefactor:
        assert(timefactor in ('h', 'd', 'm', 'y'))

    return _request('trades')
