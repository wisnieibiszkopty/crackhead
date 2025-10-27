import numpy as np
from constants import SYMBOLS_PL
from utils.decorators import forZipped


class Vernam:
    def encrypt(self, message: str):
        key = np.random.choice(list(SYMBOLS_PL), len(message))

        zipped = zip(message, key)
        resultList = []

        for (m, k) in zipped:
            encrypted_char = chr(ord(m) ^ ord(k))
            resultList.append(encrypted_char)

        return ''.join(resultList), ''.join(key)

    @forZipped
    def decrypt(self, m: str, k: str) -> str:
        return chr(ord(m) ^ ord(k))


    def encryptAlternative(self, message: str) -> str:
        key = np.random.choice(list(SYMBOLS_PL), len(message))

        zipped = zip(message, key)
        resList = []
        for (m, r) in zipped:
            resultIndex = (SYMBOLS_PL.find(m) ^ SYMBOLS_PL.find(r)) % len(SYMBOLS_PL)
            resList.append(SYMBOLS_PL[resultIndex])
        return ''.join(resList), ''.join(key)

    @forZipped
    def decryptAlternative(self, m: str, k: str) -> str:
        return SYMBOLS_PL[(SYMBOLS_PL.find(m) ^ SYMBOLS_PL.find(k)) % len(SYMBOLS_PL)]

if __name__ == "__main__":
    vernam = Vernam()

    encrypted_message, key = vernam.encrypt("Test message (Vernam)")
    print(f"Message: {encrypted_message}, key: {key}")

    decrypted_message = vernam.decrypt(encrypted_message, key)
    print("Decrypted message: ", decrypted_message)