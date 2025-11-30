import random
import sys

import pyperclip

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getRandomKey() -> str :
    symbolsList = list(SYMBOLS)
    random.shuffle(symbolsList)
    return ''.join(symbolsList)

def isKeyValid(key: str) -> bool:
    keySorted = sorted(list(key))
    symbolsList = sorted(list(SYMBOLS))
    return keySorted == symbolsList

def translateMessage(message: str, key: str, mode: str):
    translated = ''
    s1 = SYMBOLS
    s2 = key

    if mode == 'd':
        s1, s2 = s2, s1

    for symbol in message:
        if symbol.upper() in s1:
            index = s1.find(symbol.upper())

            if symbol.isupper():
                translated += s2[index].upper()
            else:
                translated += s2[index].lower()
        else:
            translated += symbol

    return translated


def interactive():
    enterKeyManually = input("Wprowadzić klucz ręcznie [y/n]: ")

    if enterKeyManually.lower().startswith('y'):
        key = input('Wprowadź klucz: ')
        isValid = isKeyValid(key)

        if not isValid:
            print("Klucz jest nieprawidłowy")
            sys.exit()
    else:
        key = getRandomKey()

    message = input('Wprowadź wiadomość: ')
    mode = input('Wprowadź tryb [e/d]: ')

    translated = translateMessage(message, key, mode)

    pyperclip.copy(translated)

    print(translated)
    print(key)


def automatic():
    message1 = "Kjcbzlv G ijtup śiglsjirt ijtvqj ugregrbqgr vsjvjilłj jkylbjilup kyzrz khłqjiugql Oygszl Urmralvzpoy LCOWDX. Vzpoyjilugr jcmpilłj vgę zl kjejbp vzlbnjiugbp Kjagmghvzl. Vlel slmagblipkrługlul mpłl trculq agsryleg i vkjvóm ajvjip, męcąb zulul ipłąbzugr ulclibp g jcmgjybp."
    key1 = "LMBCROWNGTQAEUJKFYVSHDIXPZ"
    translated1 = translateMessage(message1, key1, 'd')
    print(translated1)

    message2 = "Vidbuhmtqbd Ghcqwqrvid oh fhyids vijlfr zhthdcldweojbitekh mjzjśchtj m vodfhżjothśbq gfieikfebnqekh uqvohfjnd Ghcqwqrvid. Vijlf oet gfijgqvrse ndżyes cqoefie cqbiwę, meyłrk vgebsdctesodwecq 0 25 nhzófndbu."
    key2 = "DWBYELKUQSNCZTHGXFVORAMPJI"
    translated2 = translateMessage(message2, key2, 'd')
    print(translated2)

if __name__ == "__main__":
    #interactive()
    automatic()
