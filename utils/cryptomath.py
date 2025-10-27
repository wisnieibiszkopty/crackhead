# greatest common divisor
def gcd(a: int, b: int) -> int:
    if a > b:
        raise ArithmeticError("a > b")

    while a != 0:
        a, b = b % a, a

    return b


def findModInverse(a: int, m: int) -> int:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = u1 - q*v1, u2 - q*v2, u3 - q*v3, v1, v2, v3

    return u1 % m


if __name__ == '__main__':
    #num = gcd(32, 40)
    #print(num)

    inverse = findModInverse(3, 7)
    print(inverse)