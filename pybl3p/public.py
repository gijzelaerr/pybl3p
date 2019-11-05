from typing import Tuple, List, Dict

from pybl3p.requests import public_request


def ticker() -> (str, float, float, float, Tuple[float, float]):
    """
    Ticker.

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
    return public_request('ticker')


def orderbook() -> (List[Tuple[int, int, int]], List[Tuple[int, int, int]]):
    """
    Orderbook

    Returns:
        a tuple containing 'asks' list and 'bids' list:

            asks and bids lists both contain:

                amount: Amount BTC (*1e8)
                price: Limit price in EUR (*1e5)
                count: Count of orders at this price.
    """
    response = public_request('orderbook')
    assert response['result'] == 'success'
    return response['data']['orderbook']


def trades() -> List[Dict[str, int]]:
    """
    Last 1000 trades

    Returns:
         A list of trades.
    """
    response = public_request('trades')
    assert response['result'] == 'success'
    return response['data']['trades']


def tradehistory(timefactor: str = None, timevalue: int = None) -> List[Tuple[int, float, float]]:
    """
    Trade history

    Returns:
        A list of datapoint tuples containing:

            time:  The time of the datapoint
            price: The price of the datapoint
            volume: The volume of the datapoint
    """
    assert ((timefactor is None) == (timevalue is None))

    params = {}

    if timefactor:
        assert (timefactor in ('h', 'd', 'm', 'y'))
        params['timefactor'] = timefactor

    if timevalue:
        params['timevalue'] = timevalue

    return public_request('tradehistory', params=params)
