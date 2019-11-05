from typing import Tuple, List

from pybl3p import http_request


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
    return http_request('ticker')


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


def trades():
    """
    Last 1000 trades

    Returns:
         A list of trades.
    """
    return http_request('trades')


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

    return http_request('trades')
