from pybl3p.public import ticker, orderbook, trades, tradehistory
from unittest import TestCase


class PublicTest(TestCase):
    def test_trades(self):
        result = trades()

    def test_ticker(self):
        result = ticker()

    def test_tradehistory(self):
        result = tradehistory()

    def test_tradehistory_params(self):
        result = tradehistory(timefactor='h', timevalue=5)

    def test_orderbook(self):
        result = orderbook()
