import re

import letterMapping as lm
import wordPattern as wp
import substitutionCipher as sc

nonLetterNonSpaceCompiler = re.compile('[^A-Z\\s]')

def crackSubstitutionCipher(message):
    intersectedMap = lm.getBlankCipherletterMapping()
    cipherWordList = nonLetterNonSpaceCompiler.sub('', message.upper()).split()

    print(cipherWordList)

    for cipherWord in cipherWordList:
        pattern = wp.getWordPattern(cipherWord)

        print(pattern)

        candidates = wp.getWordsFromPattern(pattern)

        print(candidates)

        initialMap = lm.getBlankCipherletterMapping()
        candidateMap = {}

        for candidate in candidates:
            candidateMap = lm.addLettersToMapping(initialMap, cipherWord, candidate)
            initialMap = candidateMap

        print(intersectedMap)
        print(candidateMap)
        intersectedMap = lm.getQuasiIntersectedMapping(intersectedMap, candidateMap)

    return lm.removeSolvedLettersFromMapping(intersectedMap)

def decryptViaCipherletterMapping(message):
    finalMap = crackSubstitutionCipher(message)

    print('Final map:')
    print(finalMap)

    keyFormatList = ['-']*len(sc.SYMBOLS)

    for cipherLetter in finalMap:
        if len(finalMap[cipherLetter]) == 1:
            plainTextLetterId = sc.SYMBOLS.find(finalMap[cipherLetter][0])
            keyFormatList[plainTextLetterId] = cipherLetter
    retrievedKey = ''.join(keyFormatList)

    return sc.translateMessage(message, retrievedKey, 'd')

if __name__ == '__main__':
    # gkwzlsi bfuhs tdaaguks bfuh wga bfuh tdaaguk bfuh hlnalfkdux ylzg fqrgna nzfsg
    # DQNHGYWILREZCKFTJUSAMOBPXV
    cipherText = 'dallt yagj mjhazy palktca dtca'
    #cipherText = 'baoop zw lanc ocsakl'

    plainttext = decryptViaCipherletterMapping(cipherText)

    print('Plain text: ' + plainttext)