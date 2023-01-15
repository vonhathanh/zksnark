import math
from group import G


class Polynomial:
    def __init__(self, coefficient: list[float]):
        self.coefficient = coefficient

    def evaluate_step_by_step(self, x: float) -> float:
        # NOTE: this implement won't work with negative exponent
        result = 1
        polynomial = [0]*len(self.coefficient)
        for i, coeff in enumerate(self.coefficient):
            polynomial[i] = G.encrypt(x**i*self.coefficient[i])
            result *= polynomial[i]
        return result % G.p

    def evaluate(self, x: float, need_encryption: bool = True) -> float:
        # best implementation at the moment, the for loop can be improved, but we rather let it here for some
        # perfectionist to do that
        s = 0
        for i, coeff in enumerate(self.coefficient):
            s += coeff * x**i
        return G.encrypt(s) if need_encryption else s


def test_polynomial():
    p = Polynomial([2, 2, 3])  # 2 + 2x + 3x^2

    x = 5
    assert p.evaluate_step_by_step(x) == p.evaluate(x)
    x = 0
    assert p.evaluate_step_by_step(x) == p.evaluate(x)
    x = 1
    assert p.evaluate_step_by_step(x) == p.evaluate(x)


if __name__ == '__main__':
    test_polynomial()