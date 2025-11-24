import wordPattern as wp
import substitutionCipher as sc

def getBlankCipherletterMapping():
    return { letter: [] for letter in sc.SYMBOLS}

def addLettersToMapping(letterMapping, cipherWord, candidate):
    for i, symbol in enumerate(list(cipherWord)):
        if candidate[i] not in letterMapping[symbol]:
            letterMapping[symbol].append(candidate[i])
    return letterMapping

def getQuasiIntersectedMapping(mapA, mapB):
    letterMapping = getBlankCipherletterMapping()
    for letter in sc.SYMBOLS:
        setA = set(mapA[letter])
        setB = set(mapB[letter])

        if setA == set() or setB == set():
            letterMapping[letter] = list(setA | setB)
        else:
            letterMapping[letter] = list(setA & setB)
    return letterMapping

def createFinalMapping(cipherWords):
    intersectedMapping = getBlankCipherletterMapping()

    for word in cipherWords:
        pattern = wp.getWordPattern(word)
        candidates = wp.getWordsFromPattern(pattern)
        wordMapping = getBlankCipherletterMapping()

        for c in candidates:
            updatedWordMapping = addLettersToMapping(wordMapping, word, c)
            wordMapping = updatedWordMapping

        intersectedMapping = getQuasiIntersectedMapping(intersectedMapping,wordMapping)

    return intersectedMapping

def removeSolvedLettersFromMapping(map):
    loopAgain = True
    servedSolvedLetters = []

    while loopAgain:
        unservedSolvedLetters = list(filter(
            lambda k: (len(map[k]) == 1) and (k not in servedSolvedLetters),
            map
        ))

        if not unservedSolvedLetters:
            loopAgain = False
        else:
            solvedLetter = unservedSolvedLetters[0]
            respectiveLetter = map[solvedLetter][0]

            for key in map:
                if (respectiveLetter in map[key]) and (key != solvedLetter):
                    map[key].remove(respectiveLetter)
            servedSolvedLetters.append(solvedLetter)

    return map



if __name__ == "__main__":
    cipher = 'OLQIHXIRCKGNZ PLQRZKBZB MPBKSSIPLC'
    #cipher = 'TXRR CA'
    #cipher = 'BANAN TEST TE'
    cipherWords = cipher.split(' ')
    mapping = createFinalMapping(cipherWords)
    print(mapping)
    letterMap = removeSolvedLettersFromMapping(mapping)
    print(letterMap)

