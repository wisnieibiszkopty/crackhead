import os
import sys

from commonModule.primeNumbers import generateLargePrime
from utils.cryptomath import findModInverse, gcd

KEY_SIZE = 1024

def generateKeys(size):
    p = generateLargePrime(KEY_SIZE)
    q = generateLargePrime(KEY_SIZE)

    n = p * q

    while True:
        e = generateLargePrime(KEY_SIZE)

        try:
            if gcd((p-1)*(q-1), e) == 1:
                break
        except:
            print('???????')

    d = findModInverse(e, (p-1)*(q-1))

    publicKey = (n, e)
    privateKey = (n, d)

    return (publicKey, privateKey)

def makeKeyFiles(ownerName, keySize):
    if os.path.exists(f'{ownerName}_publ_key.txt') or os.path.exists(f'{ownerName}_priv_key.txt'):
        sys.exit('Uwaga: plik o nazwie {ownerName}_publ_key.txt lub {ownerName} _priv_key.txt już istnieje…')

    publicKey, privateKey = generateKeys(keySize)

    newFileObj = open(f'{ownerName}_publ_key.txt', 'w')
    newFileObj.write(f'{keySize}, {publicKey[0]}, {publicKey[1]}')
    newFileObj.close()
    newFileObj = open(f'{ownerName}_priv_key.txt', 'w')
    newFileObj.write(f'{keySize}, {privateKey[0]}, {privateKey[1]}')
    newFileObj.close()

if __name__ == '__main__':
    makeKeyFiles("kamil", KEY_SIZE)