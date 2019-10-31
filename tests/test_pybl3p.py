from pybl3p import trades
from unittest import TestCase


class Pybl3pTest(TestCase):
    def test_trades(self):
        _ = trades()

    def test_tradehistory(self):