import random

from group import G
from polynomial import Polynomial


class Verifier:
    def __init__(self, t: Polynomial, d: int, ):
        """
        :param d: degree of the polynomial p(x)
        """
        self.d = d
        self.s = random.randint(0, 2*10)
        # calculates encryption of s for all powers i in 0, 1, ..., d, i.e.: E(s^i) = g^(s^i)
        self.ES = [G.encrypt(self.s**i) for i in range(self.d)]
        # evaluates unencrypted target polynomial with s: t(s)
        self.ts = t.evaluate(self.s, need_encryption=False)