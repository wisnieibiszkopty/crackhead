import math
import random
import secrets

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

def isPrimeViaRabinMillerTest(n, trials = 5):
    t = n - 1
    s = 0
    while t % 2 == 0:
        t /= 2
        s += 1
    for trial in range(0, trials):
        b = random.randrange(2, n)
        power = pow(b, int(t), n)

        if power != 1:
            vec = []
            for i in range(0, s):
                power_ = pow(b, int(t * 2 ** i), n)
                vec.append(power_)
            if n - 1 not in vec:
                return False
    return True

def isPrimeNumber(n, omitPrimesNumber = 100, rabinMillerTrails = 10):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        LOW_PRIMES = findPrimeNumbersViaEratostenesSieve(omitPrimesNumber)

        if n > omitPrimesNumber:
            for prime in LOW_PRIMES:
                if n % prime == 0:
                    return False

        return isPrimeViaRabinMillerTest(n, rabinMillerTrails)

def generateLargePrime(keySize, omitPrimesNumber = 100, rabinMillerTrails = 10):
    isPrime = False
    triesCount = 0
    while not isPrime:
        triesCount += 1

        primeCandidate = secrets.randbits(keySize)

        if primeCandidate % 2 == 0:
            continue

        primeCandidate |= (1 << (keySize - 1))

        isPrime = isPrimeNumber(primeCandidate, omitPrimesNumber, rabinMillerTrails)

    print('Prime trial count: ', triesCount)
    return primeCandidate

def isPrimeViaRabinMillerTest_Randomized(n):
    if n < 2 or n % 2 == 0:
        return False
    if n == 3:
        return True

    t = n-1
    s = 0

    while t % 2 == 0:
        t //= 2
        s += 1
    for trial in range(0, 5):
        b = random.randrange(2, n)
        power = pow(b, t, n)
        if power != 1:
            """ vec = []
            for i in range(0, s):
                power_ = pow(b, int(t*2**i),n)
                vec.append(power_)
            if n-1 not in vec:
                return False """
            i = 0
            while power != n-1:
                if i == s-1:
                    return False
                else:
                    i += 1
                    power = pow(power, 2, n)
    return True

LOW_PRIMES = findPrimeNumbersViaEratostenesSieve(100)

def isPrimeNumber(n):
    for p in LOW_PRIMES:
        if n % p == 0:
            return False
        if n == p:
            return True
    return isPrimeViaRabinMillerTest_Randomized(n)


def generateLargePrime(keySize = 1024):
    i = 1
    while True:
        largeNum = random.randrange(pow(2, keySize-1), pow(2, keySize))
        if isPrimeNumber(largeNum):
            print('udało sie w próbie ', i)
            print('Mamy liczbę ', largeNum)
            return largeNum
            break
        i += 1

if __name__ == '__main__':
    # res = isPrimeNumber(104729)
    # print(res)

    # it takes while to generate prime for 128
    primeNumber = generateLargePrime(1024)

    print('Prime found: ', primeNumber)
    print('Is prime fr:', isPrimeNumber(primeNumber))