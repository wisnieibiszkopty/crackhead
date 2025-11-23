from affine.AffineCipher import AffineCipher
import utils.cryptomath as cm
import utils.detectEnglish as de
from constants import SYMBOLS_EN_LEN


def crackAffineCipher(ciphertext: str):
    length = SYMBOLS_EN_LEN
    affine = AffineCipher()
    englishWords = de.loadDictionary()

    for key in range(length**2):
        keyA = affine.getKeyPairs(key)[0]

        if cm.gcd(keyA, length) != 1:
            continue

        plaintext = affine.decrypt(ciphertext, key)

        if de.isEnglish(plaintext, englishWords):
            print('Potencjalny tekst jawny dla klucza: {0}: {1}'.format(key, plaintext))
            isValid = input('Potwierdź poprawność [y/n]')

            if isValid.lower().startswith('y'):
                return (key, plaintext)

    return None

if __name__ == '__main__':
    # hello works but this not
    result = crackAffineCipher("V?vIb'6?vthvkbdkIbvw'KbvU4bUv4WvQ'P'4N'v'6v'vyb6DI?vdivCDyy4N'WbvlbI466'AvJWidyP'?4dWvl4W46?byvq'W'vldyy46vq4YdWvw'6v6'4UAv'6v6b'yNwv'WUvyb6NDbvbiidy?6vNdW?4WDbv'WUv'D?wdy4?4b6v?yfv?dvpb?v'4Uv?dvw'yU-w4?v'yb'6HSwbvwDyy4N'WbAvdWbvdiv?wbvPd6?vkdRbyiDIv?dv6?y4Bbv?wbvj'y4GGb'WAvw'6v'I6dvB4IIbUv'?vIb'6?v8ovkbdkIbv4WvC'4?4Avdii4N4'I6v6'4UH")

    if result is None:
        print("Próba złamania nie powiodła się.")
    else:
        print('Klucz: {0}'.format(result[0]))
        print('Tekst jawny: {0}'.format(result[1]))