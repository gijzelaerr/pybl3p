from typing import Tuple, List, AsyncGenerator
import pandas as pd

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


def orderbook() -> (pd.DataFrame, pd.DataFrame):
    """
     The list of orders that the exchanges uses to record the interest of buyers and sellers

    Returns:
        a tuple containing 'asks' list and 'bids' DataFrames with columns:
            amount: Amount BTC (*1e8)
            price: Limit price in EUR (*1e5)
            count: Count of orders at this price.
    """
    response = public_request('orderbook')
    assert response['result'] == 'success'
    asks = pd.DataFrame(response['data']['asks'])
    bids = pd.DataFrame(response['data']['bids'])
    return asks, bids


def trades() -> pd.DataFrame:
    """
    Last 1000 trades

    Returns:
         A pandas DataFrame with trades, as columns:

            date: unix timestamp
            trade_id:
            price_int:
            amount_int:
    """
    response = public_request('trades')
    assert response['result'] == 'success'
    trades = response['data']['trades']
    df = pd.DataFrame(trades)
    df['date'] = pd.to_datetime(df['date'], unit='ms')
    df.set_index('date', inplace=True)
    return df


def tradehistory(timefactor: str = None, timevalue: int = None) -> pd.DataFrame:
    """
    Trade history

    args:
        timefactor: one of h, d, m, or y
        timevalue: the number of units

    Returns:
        A DataFrame with columns:

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

    data = public_request('tradehistory', params=params)['tradehistory']

    df = pd.DataFrame(data)
    df = df.rename(columns={'t': 'time', 'v': 'volume', 'p': 'price'})
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index('time')
    return df


def trades_stream() -> AsyncGenerator[dict, None]:
    """
    A live stream of trades.

    async generator yielding a dict containing:
            date:
            marketplace:
            price_int:
            type:
            amount_int:
    """
    return websocket_request(channel='trades')


def orderbook_stream() -> AsyncGenerator[dict, None]:
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
