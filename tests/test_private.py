from unittest import TestCase
from pybl3p.private import wallet_history, info, depth_full, orders, orders_history, trades_fetch

import logging

logging.basicConfig(level=logging.DEBUG)


class PrivateTest(TestCase):
    def test_wallet_history(self):
        wallet_history()

    def test_info(self):
        info()

    def test_depth_full(self):
        depth_full()

    def test_orders(self):
        orders()

    def test_orders_history(self):
        orders_history()

    def test_trades_fetch(self):
        trades_fetch()

    def test_trades_fetch_trade_id(self):
        trades_fetch(trade_id=1)
