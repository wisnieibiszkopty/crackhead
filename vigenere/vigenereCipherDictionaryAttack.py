from Vigenere import Vigenere
from utils.detectEnglish import loadDictionary, isEnglish
from vigenere.Vigenere import SYMBOLS_EN

SYMBOLS = SYMBOLS_EN

def dictionaryAttack(message):
    englishWords = loadDictionary()

    for word in englishWords:
        keyReplication = vigenere.generateKeyReplication(message, word)
        plaintext = vigenere.decrypt(message, keyReplication)
        correct = isEnglish(plaintext, englishWords)

        if correct:
            print(f'Potencjalnie zlamany klucz: {plaintext}')
            print(f'Dla klucza {keyReplication}')


# TODO finish
if __name__ == '__main__':
    vigenere = Vigenere()

    message = 'AivHBEsgDmdrBuGEj'
    key = 'hedonism'

    keyReplication = vigenere.generateKeyReplication(message, key)
    plaintext = vigenere.decrypt(message, keyReplication)
    print(plaintext)

    dictionaryAttack(message)

