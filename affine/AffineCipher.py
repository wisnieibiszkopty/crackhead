import utils.cryptomath as cm
import pyperclip
from constants import SYMBOLS_PL_LEN, SYMBOLS_PL

length = SYMBOLS_PL_LEN

class AffineCipher:
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

    def encrypt(self):
        pass

    def decrypt(self):
        pass