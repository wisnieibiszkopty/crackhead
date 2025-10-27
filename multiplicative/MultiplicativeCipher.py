import utils.cryptomath as cm
import pyperclip
from constants import SYMBOLS_PL_LEN, SYMBOLS_PL

length = SYMBOLS_PL_LEN

class MultiplicativeCipher:
    def run(self):
        message = input('Wiadomość: ')
        key = input('Klucz (liczba naturalna względnie pierwsza z {0}): ').format(length)

        while cm.gcd(int(key), length) != 1:
            print('Niepoprawny klucz')
            key = input('Klucz (liczba naturalna względnie pierwsza z {0}): ').format(length)

        mode = input('encyption/decryption mode [e/d]')

        outcome = ''
        if mode == 'e':
            outcome = self.encrypt(message, int(key))
        elif mode == 'd':
            outcome = self.decrypt(message, int(key))

        pyperclip.copy(outcome)
        print('Result: ', outcome)

    def encrypt(self, message: str, key: int) -> str:
        encrypted = ''
        for symbol in message:
            index = SYMBOLS_PL.find(symbol)
            multipliedIndex = index * key % length
            encrypted += SYMBOLS_PL[multipliedIndex]

        return encrypted

    def decrypt(self, message: str, key: int) -> str:
        decrypted = ''
        modInverseKey = cm.findModInverse(key, length)

        for symbol in message:
            index = SYMBOLS_PL.find(symbol)
            invertedMultiplicationIndex = index * modInverseKey % length
            decrypted += SYMBOLS_PL[invertedMultiplicationIndex]

        return decrypted

if __name__ == '__main__':
    multiplicative = MultiplicativeCipher()
    multiplicative.run()