import math


class EncryptedUnit:
    def __init__(self, value: int):
        self.value = value


class Group:
    def __init__(self, p: int, g: int, operations: list[str] = ()):
        """
        :param p: prime number
        :param g: generator
        :param operations: which operations do the group support? could be an array of: add, multi, division...
        """
        self.p = p
        self.g = g
        self.operations = operations

    def encrypt(self, x: int) -> int:
        return int(math.pow(self.g, x)) % self.p

    def multi(self, a: int, b: int) -> int:
        return self.encrypt(a*b) % self.p

    def add(self, a: int, b: int) -> int:
        return (self.encrypt(a+b)) % self.p


def test_add():
    group = Group(7, 5, ["+", "*"])
    print(group.add(3, 2))
    print(group.add(1, 4))
    print(group.add(4, 6))
    print(group.add(8, 2))


if __name__ == '__main__':
    test_add()


