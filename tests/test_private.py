from unittest import TestCase
from pybl3p.private import wallet_history

import logging

logging.basicConfig(level=logging.DEBUG)


class PrivateTest(TestCase):
    def teste_wallet_history(self):
        wallet_history()
