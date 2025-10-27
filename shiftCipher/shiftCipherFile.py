from shiftCipher.ShiftCipher import ShiftCipher
import time, os, sys

def shiftCipherFile():
    mode = input('Mode [e/d]: ')
    inputFileName = input('Enter input file name: ')
    outputFileName = input('Enter output file name: ')
    key = int(input('Enter key: '))

    startTime = time.time()

    with open('files/' + inputFileName, 'r') as inputFile:
        shiftCipher = ShiftCipher()
        encrypted_text = ''
        if mode == 'e':
            encrypted_text += shiftCipher.encrypt(inputFile.read(), key)
        elif mode == 'd':
            encrypted_text += shiftCipher.decrypt(inputFile.read(), key)

        with open('files/' + outputFileName, 'w') as outputFile:
            outputFile.write(encrypted_text)

    endTime = time.time()
    elapsedTime = endTime - startTime
    print('Elapsed time:', elapsedTime)

if __name__ == '__main__':
    shiftCipherFile()
