from group import G
from polynomial import Polynomial


if __name__ == '__main__':
    s = 4
    d = 2
    encrypted_s = [G.encrypt(s**i) for i in range(d+1)]
    print(f"encrypted s: {encrypted_s}")

    p = Polynomial([-2, 3, 5])
    print(f"evaluation of s = {s} is {p.evaluate(s)}")

    eps = 1
    for i, coeff in enumerate(p.coefficient):
        eps *= encrypted_s[i] ** coeff

    print(f"evaluation of encrypted s: {eps%G.p}")
