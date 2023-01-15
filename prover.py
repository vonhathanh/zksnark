from polynomial import Polynomial
from group import G


class Prover:
    def __init__(self, p: Polynomial, t: Polynomial):
        self.p = p
        self.t = t

    def setup(self, es: list[float]) -> tuple[float, float]:
        """
        :param es: encrypted values of s for all powers i in 0, 1, ..., d, i.e.: E(s^i) = g^(s^i)
        """
        h = self.p.divide(self.t)
        eps = 1
        for i, coeff in enumerate(self.p.coefficient):
            eps *= G.encrypt(es[i] ** coeff)

        ehs = 1
        for i, coeff in enumerate(h.coefficient):
            ehs *= G.encrypt(es[i] ** coeff)
        return eps, ehs
