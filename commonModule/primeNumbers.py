import math
import random

import utils.cryptomath

def isPrimeNumberViaDivisionTest(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print('Divided by: ', i)
            return False
    return True

def findPrimeNumbersViaEratostenesSieve(n):
    m = math.ceil(n/2)
    s = [1] * m
    i = 1
    p = 3
    q = 4

    while q < m:
        if s[i-1] != 0:
            j = q - 1
            while j < m:
                s[j] = 0
                j += p
        i += 1
        p += 2
        q += 2 * (p-1)

    return getPrimeNumbersFromVector(s)

def getPrimeNumbersFromVector(vec):
    primeNumbers = []
    for index, num in enumerate(vec):
        if num != 0:
            primeNumbers.append((index * 2) + 1)

    primeNumbers.pop(0)
    return primeNumbers

def isPrimeViaFermatTest(n):
    b = n
    while utils.cryptomath.gcd(b, n) != 1:
        b = random.randrange(2, n)
    power = pow(b, n-1, n)
    return power == 1

def isPrimeViaRabinMillerTest(n):
    pass

def isPrimeNumberViaRabinMillerTest(n):
    pass

if __name__ == '__main__':
    # res = isPrimeNumberViaDivisionTest(1000007)
    # print(res)

    # res = findPrimeNumbersViaEratostenesSieve(18)
    # print(res)

    res = isPrimeViaFermatTest(561)
    print(res)