from pybl3p.public import ticker, orderbook, trades, tradehistory
from unittest import TestCase


class PublicTest(TestCase):
    def test_trades(self):
        _ = trades()

    def test_ticker(self):
        _ = ticker()

    def test_tradehistory(self):
        _ = tradehistory()

    def test_orderbook(self):
        _ = orderbook()