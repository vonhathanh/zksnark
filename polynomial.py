import math
from group import Group


class Polynomial:
    def __init__(self, coefficient: list[float]):
        self.coefficient = coefficient
        self.group = Group(7, 5, ["+", "*"])

    def evaluate_step_by_step(self, x: float) -> float:
        result = 1
        polynomial = [0]*len(self.coefficient)
        for i, coeff in enumerate(self.coefficient):
            polynomial[i] = self.group.encrypt(x**i*self.coefficient[i])
            result *= polynomial[i]
        return result % self.group.p

    def evaluate(self, x: float) -> float:
        s = 0
        for i, coeff in enumerate(self.coefficient):
            s += coeff * x**i
        return self.group.encrypt(s)


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