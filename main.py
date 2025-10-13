from cesear.Cesar import Cesar
from cesear.caesarCipherCrack import *

def cesar_func():
    message = input('message: ')
    key = input('key: ')
    mode = input('encrypt/decrypt [e/d]:')

    cesar = Cesar()

    if mode == 'e':
        encryption = cesar.encrypt(message, int(key))
        print(encryption)
    elif mode == 'd':
        decryption = cesar.decrypt(message, int(key))
        print(f'decrypted message {decryption}')


def main():
    #cesar_func()
    message = input('message: ')
    crackCaesarCipher(message)


if __name__ == '__main__':
    main()