# default prime number
PrimeNumber = 13
# default generator
Generator = 10


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
        return self.g**x % self.p

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


def test_multi():
    group = Group(7, 5, ["+", "*"])
    print(group.multi(3, 2))
    print(group.multi(2, 3))
    print(group.multi(1, 1))
    print(group.multi(8, 2))


G = Group(PrimeNumber, Generator)

if __name__ == '__main__':
    test_add()
    test_multi()


