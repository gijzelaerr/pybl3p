from typing import Tuple, List, Dict

from pybl3p.requests import public_request, websocket_request


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
    return response['data']


def trades() -> List[Dict[str, int]]:
    """
    Last 1000 trades

    Returns:
         A list of trades represented as a dicts, with keys:

            date: unix timestamp
            trade_id:
            price_int:
            amount_int:
    """
    response = public_request('trades')
    assert response['result'] == 'success'
    return response['data']['trades']


def tradehistory(timefactor: str = None, timevalue: int = None) -> List[Tuple[int, float, float]]:
    """
    Trade history

    args:
        timefactor: one of h, d, m, or y
        timevalue: the number of units

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

    return public_request('tradehistory', params=params)['tradehistory']


def trades_stream():
    """
    A live stream of trades.

    async yields:
        a dict containing:
            date:
            marketplace:
            price_int:
            type:
            amount_int:
    """
    return websocket_request(channel='trades')


def orderbook_stream():
    """
    A live stream of orderbook updates

    async yields:
        a dict containing:
            asks:
                a list of dicts containing price_int and amount_int key values
            bids:
                a list of dicts containing price_int and amount_int key values
    """
    return websocket_request(channel='orderbook')
