import operator

from constants import SYMBOLS_EN_UPPER

SYMBOLS = SYMBOLS_EN_UPPER
ETAOIN = 'ETAOINSHRDLUCMFWYPVBGKQJXZ'

def getLetterCount(message):
    return { letter: 0 for letter in SYMBOLS}

def getFrequencyOrder(message):
    messageDict = getLetterCount(message)

    for symbol in message.upper():
        if symbol in SYMBOLS:
            messageDict[symbol] += 1

    lettersSortedList = sorted(messageDict.items(), key = operator.itemgetter(1), reverse=True)
    lettersSortedDict = dict(lettersSortedList)

    print(lettersSortedDict)

    etaionOrderedSortedList = []
    for freq in set(lettersSortedDict.values()):
        lettersWithThatFreq = list(filter(
            lambda k: lettersSortedDict[k] == freq,
            lettersSortedDict.keys()
        ))

        lettersWithThatFreq.sort(key=ETAOIN.find)
        etaionOrderedSortedList = lettersWithThatFreq + etaionOrderedSortedList

    return ''.join(etaionOrderedSortedList)

def getEnglishFrequencyMatchScore(message):
    messageFrequencyOrder = getFrequencyOrder(message)
    matchScore = 0
    frequentLetters = ETAOIN[:6]
    rareLetters = ETAOIN[-6:]

    for letter in messageFrequencyOrder[:6]:
        if letter in frequentLetters:
            matchScore += 1
    for letter in messageFrequencyOrder[-6:]:
        if letter in rareLetters:
            matchScore += 1

    return matchScore



if __name__ == '__main__':
    print(getFrequencyOrder('HELLO WORLD'))
    print(getEnglishFrequencyMatchScore('one two three four five six seven eight'))
    # TODO lab 4