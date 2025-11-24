import re
from pydoc import plaintext

import letterMapping as lm
import wordPattern as wp
import substitutionCipher as sc

nonLetterNonSpaceCompiler = re.compile('[^A-Z\\s]')

def crackSubstitutionCipher(message):
    intersectedMap = lm.getBlankCipherletterMapping()
    cipherWordList = nonLetterNonSpaceCompiler.sub('', message.upper()).split()

    for cipherWord in cipherWordList:
        pattern = wp.getWordPattern(cipherWord)
        candidates = wp.getWordsFromPattern(pattern)
        initialMap = lm.getBlankCipherletterMapping()
        candidateMap = {}

        for candidate in candidates:
            candidateMap = lm.addLettersToMapping(initialMap, cipherWord, candidate)
            initialMap = candidateMap

        intersectedMap = lm.getQuasiIntersectedMapping(intersectedMap, candidateMap)

    return lm.removeSolvedLettersFromMapping(intersectedMap)

def decryptViaCipherletterMapping(message, letterMapping):
    finalMap = crackSubstitutionCipher(message)
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
    cipherText = 'gkwzlsi bfuhs tdaaguks bfuh wga bfuh tdaaguk bfuh hlnalfkdux ylzg fqrgna nzfsg'
    letterMapping = crackSubstitutionCipher(cipherText)
    print(letterMapping)
    plainttext = decryptViaCipherletterMapping(cipherText, letterMapping)

    print('Plain text: ' + plainttext)