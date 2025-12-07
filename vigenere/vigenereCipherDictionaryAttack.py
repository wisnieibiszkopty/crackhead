from Vigenere import Vigenere
from utils.detectEnglish import loadDictionary, isEnglish
from vigenere.Vigenere import SYMBOLS_EN

SYMBOLS = SYMBOLS_EN

def dictionaryAttack(message):
    englishWords = loadDictionary()

    for word in englishWords.keys():
        keyReplication = vigenere.generateKeyReplication(message, word.upper())
        plaintext = vigenere.decrypt(message, keyReplication)
        correct = isEnglish(plaintext, englishWords)

        if correct:
            print(f'Potential cracked message: {plaintext}')
            print(f'For key: {keyReplication}')


if __name__ == '__main__':
    vigenere = Vigenere()

    message = 'mHZWMwSA50CQZHV3CC1TYZZUAHROCR1B3T1JKDL8WTQSLZNwLA55IU5uSPNQXELoWNQIVYFwZHVF2TKMVYLQ1SL43EIE04CQLuuSMw,OSMQVAA5OCfNELgWTJu6QCVNELmQPMSLTOPOTVOCCAP9ZNQ1NUFQPZE9P1VAI5F2JKuWLVVGS\'FOGTRVFIPJu!W2KSA PT1AP9PKKVI L2GJuRYCC2A3LVENELZNwTE,FNCTTR47wHO6V1wGNUFIWZH631AAdYT1wNA0FTGJu ZCJOSL1WR1LR3CKJE55QHOCR5QQTuR4CVNEL"NCZHV3"wUFLXWFKR5FNCTTR47wRI PZCZU9PGw,ELT1w3IUPT1ARVRITJEUFIUAO5PCQLu SMwSO05CKTF36MPZIRWCC1TYZZUAOWFINRu TUGEu'
    #key = 'garlic'

    #keyReplication = vigenere.generateKeyReplication(message, key)
    #plaintext = vigenere.decrypt(message, keyReplication)
    #print(plaintext)

    dictionaryAttack(message)

