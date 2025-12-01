from constants import SYMBOLS_PL, SYMBOLS_EN

SYMBOLS = SYMBOLS_EN

class Vigenere:
    def run(self, automatic: bool = False, messageInput="", keyInput="", mode="e"):
        if(automatic):
            message = messageInput
            key = keyInput
        else:
            message = input('message: ')
            key = input('key: ')
            mode = input('encrypt/decrypt [d/e]:')

        keyReplication = self.generateKeyReplication(message, key)

        if mode == 'e':
            return self.encrypt(message, keyReplication)
        elif mode == 'd':
            return self.decrypt(message, keyReplication)
        return None

    def generateKeyReplication(self, message: str, key: str) -> str:
        #message = message.upper()
        #key = key.upper()

        div = len(message) // len(key)
        mod = len(message) % len(key)
        return key * div + key[0:mod]

    def encrypt(self, message: str, keyReplication: str) -> str:
        #message = message.upper()
        #keyReplication = keyReplication.upper()

        zipped = zip(message, keyReplication)
        resultList = []

        for (m, k) in zipped:
            if m in SYMBOLS:
                resultIndex = (SYMBOLS.find(m) + SYMBOLS.find(k)) % len(SYMBOLS)
                resultList.append(SYMBOLS[resultIndex])
            else:
                resultList.append(m)

        return ''.join(resultList)

    def decrypt(self, message: str, keyReplication: str) -> str:
        #message = message.upper()
        #keyReplication = keyReplication.upper()

        zipped = zip(message, keyReplication)
        resultList = []

        for (m, k) in zipped:
            if m in SYMBOLS:
                resultIndex = (SYMBOLS.find(m) - SYMBOLS.find(k)) % len(SYMBOLS)
                resultList.append(SYMBOLS[resultIndex])
            else:
                resultList.append(m)

        return ''.join(resultList)


if __name__ == "__main__":


    vigenere = Vigenere()

    # user input use case
    result = vigenere.run()
    print(result)

    # auto encryption and decryption
    key = "Vigenere"
    message = "War is peace. Freedom is slavery. Ignorance is strength."
    keyReplication = vigenere.generateKeyReplication(message, key)
    encrypted_message = vigenere.encrypt(message, keyReplication)
    decrypted_message = vigenere.decrypt(encrypted_message, keyReplication)
    print("Decrypted message: ", decrypted_message)

    encrypted_messages = [
        "kzU0e!4U0a2iĘUwżi3Bm832Y",
        "WOnFŁdęA?kVOĄźRsO?0YŚĆĆ0ćbDłjVn0ŚE?MŃń9ĘÓKDLŻL?ŃUDOFPH.ŃEńK0NĆ,ń03I1FDhCIbLbPLĘU0MĄp!C?Odńt6DASĆdęŃCH,ńŚźłoJ.ćLE?kKZRĘUxÓ7mMdFYbFŃCŚ7ÓNuMdFGNW!ĘłzM!ńŚ0GL7ńR0D2CĆ0ŃL!kGFRDEKÓRxDNŃkVOĄźRsO?Żh",
        "łb6DW,YMwJRŁoŚwIjLMdYÓbRYKGPĘłżWąęFGńbV!ŃI0IźCD,YŚpbR1eł.MłOŻrMŻ?ROGąD8łxŃMr1ÓźbPFeIFłŃFŚv1Óbbm1ąMĄZgępdACtIhKodŁg!h"
    ]
    keys = [
        "PIZZA",
        "ToNieVigenere",
        "ToGiovanBelaso"
    ]

    zipped = zip(encrypted_messages, keys)

    for (message, key) in zipped:
        decrypted_message = vigenere.run(automatic=True, messageInput=message, keyInput=key, mode="d")
        print(decrypted_message)


