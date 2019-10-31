from pybl3p import trades, tradehistory, ticker
from unittest import TestCase


class Pybl3pTest(TestCase):
    def test_trades(self):
        _ = trades()

    def test_ticker(self):
        _ = ticker()

    def test_tradehistory(self):
        _ = tradehistory()
