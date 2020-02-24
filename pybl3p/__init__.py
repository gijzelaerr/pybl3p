__version__ = '0.3'

from .private import (
    deposit_address,
    depth_full,
    info,
    new_deposit_address,
    order_add,
    order_cancel,
    order_result,
    orders,
    orders_history,
    trades_fetch,
    wallet_history,
    withdraw
)

from .public import (
    orderbook,
    orderbook_stream,
    ticker,
    tradehistory,
    trades,
    trades_stream
)
