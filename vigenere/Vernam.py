import numpy as np
from constants import SYMBOLS_PL


class Vernam:
    def encrypt(self, message: str):
        key = np.random.choice(list(SYMBOLS_PL), len(message))

        zipped = zip(message, key)
        resultList = []

        for (m, k) in zipped:
            encrypted_char = chr(ord(m) ^ ord(k))
            resultList.append(encrypted_char)

        return ''.join(resultList), ''.join(key)


    def decrypt(self, message: str, key: str) -> str:
        zipped = zip(message, key)
        resultList = []

        for (m, k) in zipped:
            decrypted_char = chr(ord(m) ^ ord(k))
            resultList.append(decrypted_char)

        return ''.join(resultList)

    def encryptAlternative(self, message: str) -> str:
        key = np.random.choice(list(SYMBOLS_PL), len(message))

        zipped = zip(message, key)
        resList = []
        for (m, r) in zipped:
            resultIndex = (SYMBOLS_PL.find(m) ^ SYMBOLS_PL.find(r)) % len(SYMBOLS_PL)
            resList.append(SYMBOLS_PL[resultIndex])
        outcome = ''.join(resList)
        return outcome, ''.join(key)

    def decryptAlternative(self, message: str, key: str) -> str:
        zipped = zip(message, key)
        resList = []
        for (c, r) in zipped:
            resultIndex = (SYMBOLS_PL.find(c) ^ SYMBOLS_PL.find(r)) % len(SYMBOLS_PL)
            resList.append(SYMBOLS_PL[resultIndex])
        outcome = ''.join(resList)
        return outcome

if __name__ == "__main__":
    vernam = Vernam()

    encrypted_message, key = vernam.encrypt("Test message (Vernam)")
    print(f"Message: {encrypted_message}, key: {key}")

    decrypted_message = vernam.decrypt(encrypted_message, key)
    print("Decrypted message: ", decrypted_message)