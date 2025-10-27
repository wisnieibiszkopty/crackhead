import pyperclip, math

class ShiftCipher:
    def run(self):
        message = input('Enter the message: ')
        key = int(input('Enter the key <2, len(message -)>: '))
        mode = input('Enter the mode [e/d]: ')

        if mode == 'e':
            encrypted_message = self.encrypt(message, key)
            print("Encrypted message:", encrypted_message)
            pyperclip.copy(encrypted_message)
        elif mode == 'd':
            decrypted_message = self.decrypt(message, key)
            print("Decrypted message:", decrypted_message)
            pyperclip.copy(decrypted_message)

    def encrypt(self, message: str, key: int) -> str:
        resList = ['']*key

        for i in range(len(message)):
            j = i % key
            resList[j] += message[i]

        return ''.join(resList)

    def decrypt(self, cipher: str, key: int) -> str:
        cipherLength = len(cipher)
        columnsNumber = math.ceil(cipherLength / key)
        rowsNumber = key
        emptyCellsNumber = rowsNumber * columnsNumber - cipherLength
        resList = ['']*columnsNumber

        h = 0
        for i in range(cipherLength):
            currentRowNo = (i+h) // columnsNumber
            currentColNo = (i+h) % columnsNumber

            if(currentRowNo >= rowsNumber - emptyCellsNumber) and (currentColNo == columnsNumber - 1):
                h += 1
                resList[0] += cipher[i]
            else:
                resList[currentColNo] += cipher[i]

        return ''.join(resList)

if __name__ == "__main__":
    shift = ShiftCipher()
    shift.run()