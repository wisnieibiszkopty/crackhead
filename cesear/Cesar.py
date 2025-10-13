from constants import *

class Cesar:
    def run(self, message: str, key: int, mode: int):
        result = ''
        for symbol in message:
            if symbol in SYMBOLS_PL:
                symbolIndex = SYMBOLS_PL.find(symbol)
                result += SYMBOLS_PL[(symbolIndex + (-1)**(mode + 1)*key) % SYMBOLS_LEN]
            else:
                result += symbol

        return result

    def encrypt(self, message: str, key: int) -> str:
        return self.run(message, key, 0)

    def decrypt(self, message: str, key: int) -> str:
        return self.run(message, key, 1)