from typing import Tuple
from pybl3p.requests import private_request
import pandas as pd


def error_check(response: dict) -> dict:
    if response['result'] != 'success':
        raise Exception(response['data'])
    else:
        return response['data']


def order_add(type_: str, amount: int = None, price: int = None, amount_funds: int = None,
              fee_currency: str = 'EUR',
              market: str = 'BTCEUR'):
    """
    Create an order

    args:
        type_: ask or bid
        amount: Amount in BTC or LTC. When omitted, amount_funds is required. Also note that this field and the
                amount_funds field cannot both be set when the price field is also set. When the price field is not set
                this field can be set when amount_funds is also set.
        price: Limit price in EUR (*1e5)
        amount_funds: When omitted, amount is required. Also note that this field and the amount field cannot
                      both be set when the price field is also set. When the price field is not set this field can be
                      set when amount is also set.
        market: BTCEUR or LTCEUR
    """
    assert type_ in ('ask', 'bid')
    assert market in ('BTCEUR', 'LTCEUR')
    assert fee_currency in ('BTC', 'EUR')
    assert bool(amount) or bool(amount_funds)  # make sure one it set
    if bool(price):
        assert bool(amount) != bool(amount_funds)  # make sure only one is set if price is given
    params = {'type': type_, 'fee_currency': fee_currency}
    if amount:
        params['amount_int'] = amount
    if price:
        params['price_int'] = price
    if amount_funds:
        params['amount_funds_int'] = amount_funds

    data = private_request(callname='order/add', market=market, params=params)
    return error_check(data)['order_id']


def order_cancel(order_id: int, market: str = 'BTCEUR'):
    """
    Cancel an order
    """
    assert market in ('BTCEUR', 'LTCEUR')
    params = {'order_id': order_id}
    data = private_request(callname='order/cancel', market=market, params=params)
    return error_check(data)


def order_result():
    """
    Get a specific order
    """
    raise NotImplemented


def depth_full(market: str = 'BTCEUR') -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Get the whole orderbook

    Returns:
        a asks and bids pandas Dataframe, each with the columns:

            amount: Amount BTC (*1e8)
            price: Limit price in EUR (*1e5)
            count: Count of orders at this price.
    """
    assert market in ('BTCEUR', 'LTCEUR', 'GENMKT')
    data = private_request(callname='depth/full', market=market)
    checked = error_check(data)
    asks = checked['asks']
    bids = checked['bids']
    return pd.DataFrame(asks), pd.DataFrame(bids)


def wallet_history(currency: str = 'EUR', page: int = 1):
    """
    get the transaction history

    args:
        currency: Currency of the wallet. (Can be: 'BTC', 'EUR')
        page: Page number. (1 = most recent transactions)

    """
    params = {'currency': currency, 'page': page}
    data = private_request(callname='wallet/history', market='GENMKT', params=params)
    return error_check(data)


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


def info() -> dict:
    """
    Get account info & balance
    """
    data = private_request(callname='info', market='GENMKT')
    return error_check(data)


def orders(market: str = 'BTCEUR') -> pd.DataFrame:
    """
    Get active orders.

    args:
        market: BTCEUR or LTCEUR

    returns:
        A DataFrame with columns:

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
    assert market in ('BTCEUR', 'LTCEUR')
    data = private_request(callname='orders', market=market)
    return pd.DataFrame(error_check(data)['orders'])


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
