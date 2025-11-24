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

def removeSolvedLettersFromMapping(letterMapping):
    pass


if __name__ == "__main__":
    print(addLettersToMapping(getBlankCipherletterMapping(), 'HGHHU', 'NANNY'))

    cipherWord = "HGHF"

    candidate1 = "THAT"
    emptyMapping1 = getBlankCipherletterMapping()
    result1 = addLettersToMapping(emptyMapping1, cipherWord, candidate1)

    candidate2 = "HIGH"
    emptyMapping2 = getBlankCipherletterMapping()
    result2 = addLettersToMapping(emptyMapping2, cipherWord, candidate2)

    finalMap = getQuasiIntersectedMapping(result1, result2)
    print(finalMap)

