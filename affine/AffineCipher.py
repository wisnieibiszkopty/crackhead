import utils.cryptomath as cm
import pyperclip

from constants import SYMBOLS_EN

length = len(SYMBOLS_EN)

class AffineCipher:
    def run(self):
        message = input('Wiadomość: ')

        # 241
        key = input('Klucz (liczba całkowita): ')

        mode = input('encyption/decryption mode [e/d]')

        outcome = ''
        if mode == 'e':
            outcome = self.encrypt(message, int(key))
        elif mode == 'd':
            outcome = self.decrypt(message, int(key))

        pyperclip.copy(outcome)
        print('Result: ', outcome)

    def getKeyPairs(self, key):
        keyA = key // length
        keyB = key % length
        return (keyA, keyB)

    def validateKeys(self, keyA: int, keyB: int, mode: str) -> str | None:
        if keyA == 1 and mode == 'e':
            return 'keyA nie może mieć wartości 1'
        elif keyB == 0 and mode == 'e':
            return 'keyB nie może mieć wartości 0'
        elif keyA < 0 or keyB < 0 or keyB > length:
            return 'Obie części klucza muszą być dodatnie'
        elif cm.gcd(keyA, length) != 1:
            return 'Część keyA musi być względnie pierwsza z długością alfabetu {0}'.format(length)
        else:
            return None

    def encrypt(self, message, key) -> str:
        keyA, keyB = self.getKeyPairs(key)
        validationResult = self.validateKeys(keyA, keyB, 'e')

        if validationResult is not None:
            print(validationResult)
            raise AssertionError

        cipherText = ''

        for symbol in message:
            if symbol in SYMBOLS_EN:
                symbolIndex = SYMBOLS_EN.find(symbol)
                cipherText += SYMBOLS_EN[(symbolIndex * keyA + keyB) % length]
            else:
                cipherText += symbol

        pyperclip.copy(cipherText)

        return cipherText

    def decrypt(self, message, key):
        keyA, keyB = self.getKeyPairs(key)
        validationResult = self.validateKeys(keyA, keyB, 'd')

        if validationResult is not None:
            print(validationResult)
            raise AssertionError

        plainText = ''
        modMultiplicationInverseOfKeyA = cm.findModInverse(keyA, length)

        for symbol in message:
            if symbol in message:
                symbolIndex = SYMBOLS_EN.find(symbol)
                plainText += SYMBOLS_EN[((symbolIndex - keyB) * modMultiplicationInverseOfKeyA) % length]
            else:
                plainText += symbol

        return plainText

if __name__ == '__main__':
    affine = AffineCipher()
    affine.run()