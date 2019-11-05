from typing import List, Tuple
from pybl3p.requests import private_request
from datetime import datetime


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


def depth_full(market: str = 'GENMKT'):
    """
    Get the whole orderbook

    Returns:
        a tuple containing 'asks' list and 'bids' list:

            asks and bids lists both contain:

                amount: Amount BTC (*1e8)
                price: Limit price in EUR (*1e5)
                count: Count of orders at this price.
    """
    return private_request(callname='depth/full', market=market)


def wallet_history(currency: str = 'EUR', page: int = 1):
    """
    get the transaction history

    args:
        currency: Currency of the wallet. (Can be: 'BTC', 'EUR')
        page: Page number. (1 = most recent transactions)

    """
    params = {'currency': currency, 'page': page}
    return private_request(callname='wallet/history', market='GENMKT', params=params)


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
    return private_request(callname='info', market='GENMKT')


def orders(market: str = 'GENMKT') -> List[
    Tuple[int, str, str, str, str, str, datetime, float, float, float, float, float]]:
    """
    Get active orders

    returns:
        A list of tuples containing:

            order_id: Id of the order.
            label: API-key label
            currency: Currency of the order. (Is now by default 'EUR')
            item: The item that will be traded for `currency`. (Can be: 'BTC')
            type: Type of order. (Can be: 'bid', 'ask')
            status: Status of the order. (Can be: ‘open’, ’placed’)
            date: The time the order got added.
            amount: Total order amount of BTC or LTC.
            amount_funds_executed: Amount in funds that is executed.
            amount_executed: Amount that is executed.
            price: Order limit price.
            amount_funds: Maximal EUR amount to spend (*1e5)
    """
    return private_request(callname='orders', market=market)


def orders_history(
        page: int = None,
        date_from: int = None,
        date_to: int = None,
        recs_per_page: int = None,
        market: str = 'GENMKT',
):
    """
    Get order history

    args:
        page: Page number. (1 = most recent transactions)
        date_from: Filter the result by a Unix-timestamp. Transactions before this date will not be returned.
        date_to: Filter the result by a Unix-timestamp. Transactions after this date will not be returned.
        recs_per_page: Number of records per page.

    returns:
        A tuple containing:

            page: Current page number.
            records: Count of records in the result set.
            max_page: Number of last page.
            orders: Array of active orders.

    """
    params = {}

    if page:
        params['page'] = page

    if date_from:
        params['date_from'] = date_from

    if date_to:
        params['date_to'] = date_to

    if recs_per_page:
        params['recs_per_page'] = recs_per_page

    return private_request(callname='orders/history', market=market, params=params)


def trades_fetch(
        trade_id: int = None,
        market: str = 'GENMKT',

):
    """
    Fetch all trades on BL3P
    """
    params = {}

    if trade_id:
        params['trade_id'] = trade_id
    return private_request(callname='orders/history', market=market, params=params)
