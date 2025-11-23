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
    result = crackAffineCipher('XLkkw')

    if result is None:
        print("Próba złamania nie powiodła się.")
    else:
        print('Klucz: {0}'.format(result[0]))
        print('Tekst jawny: {0}'.format(result[1]))