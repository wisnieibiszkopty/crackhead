from constants import SYMBOLS_PL, SYMBOLS_LEN


class Vigenere:
    def run(self):
        message = input('message: ')
        key = input('key: ')
        mode = input('encrypt/decrypt [1/0]:')

        div = len(message) // len(key)
        mod = len(message) % len(key)
        keyReplication = key * div + key[0:mod]

        if mode == 'e':
            self.encrypt(message, keyReplication)
        elif mode == 'd':
            self.decrypt(message, keyReplication)

    def encrypt(self, message: str, keyReplication: str):
        zipped = zip(message, keyReplication)
        resultList = []

        for (m, k) in zipped:
            if m in SYMBOLS_PL:
                resultIndex = (SYMBOLS_PL.find(m) + SYMBOLS_PL.find(k)) % len(SYMBOLS_PL)
                resultList.append(SYMBOLS_PL[resultIndex])
            else:
                resultList.append(m)

        return ''.join(resultList)

    def decrypt(self, message: str, keyReplication: str):
        zipped = zip(message, keyReplication)
        resultList = []

        for (m, k) in zipped:
            if m in SYMBOLS_PL:
                resultIndex = (SYMBOLS_PL.find(m) - SYMBOLS_PL.find(k)) % len(SYMBOLS_PL)
                resultList.append(SYMBOLS_PL[resultIndex])
            else:
                resultList.append(m)

        return ''.join(resultList)