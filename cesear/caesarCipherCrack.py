from cesear.Cesar import Cesar
from constants import SYMBOLS_LEN

def crackCaesarCipher(message: str):
    cesar = Cesar()
    for i in range(SYMBOLS_LEN):
        decryptedMessage = cesar.decrypt(message, i)
        print(f'Key: {i}, message {decryptedMessage}')
