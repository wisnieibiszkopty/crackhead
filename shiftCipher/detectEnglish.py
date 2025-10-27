from constants import SYMBOLS_EN


def loadDictionary():
    with open('files/dictionary.txt', 'r') as file:
        content = file.read()
        contentList = content.split('\n')

        englishWords = { word: None for word in contentList }
        return englishWords


def removeNonLetters(message: str):
    lettersOnly = []
    for symbol in message:
        if symbol in SYMBOLS_EN:
            lettersOnly.append(symbol)

    return ''.join(lettersOnly)


def getEnglishCount(message: str, englishWords) -> float:
    potentialWordsList = removeNonLetters(message).split()

    if potentialWordsList == []:
        return 0.0

    matches = 0
    for word in potentialWordsList:
        if word.upper() in englishWords:
            matches += 1

    return matches / len(potentialWordsList)


def isEnglish(message: str, englishWords, wordsPercentage = 50, lettersPercentage = 60) -> bool:
    wordsMatch = getEnglishCount(message, englishWords) * 100 >= wordsPercentage
    lettersMatch = (len(removeNonLetters(message)) / len(message) * 100 >= lettersPercentage)

    return wordsMatch and lettersMatch


if __name__ == '__main__':
    englishWords = loadDictionary()
    message = "Hello, i am under the water"
    english = isEnglish(message, englishWords)
    print(message)
    print(english)

