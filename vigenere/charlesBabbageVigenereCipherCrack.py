import sys
import frequencyAnalysis as fa
import Vigenere
from operator import itemgetter
import itertools

testMsg= 'PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'

def getConcatenatedEveryNthLetter(message, keyLength, n):
    subSequence = [message[i] for i in range(n-1, len(message), keyLength)]
    return ''.join(subSequence)

print(getConcatenatedEveryNthLetter(testMsg, 4, 1))
# PAEBABANZIAHAKDXAAAKIU

def attemptCrackWithKeyLength(ciphertext, keyLength):
    ciphertextUp = ciphertext.upper()
    allFrequencyScores = []

    vigenere = Vigenere.Vigenere()
    #freqAnal = fa.FrequencyAnalyzer()

    # I etap: poszukiwanie zbioru potencjalnych kluczy o dł. keyLength
    for n in range(1, keyLength + 1): # n to numer porz. litery klucza
        print(n)
        submessage_n = getConcatenatedEveryNthLetter(ciphertextUp, keyLength, n)

        frequencyScoresForSubmessage_n = []
        for subKey in Vigenere.SYMBOLS: # sybKey to 1-literowy podciąg klucza
            keyReplication = vigenere.generateKeyReplication(submessage_n, submessage_n)
            decryptedSubmessage_n = vigenere.decrypt(submessage_n,keyReplication)
            tuple_ = (subKey, fa.getEnglishFrequencyMatchScore(decryptedSubmessage_n))
            frequencyScoresForSubmessage_n.append(tuple_)

        frequencyScoresForSubmessage_n.sort(key = itemgetter(1), reverse = True)

        allFrequencyScores.append(frequencyScoresForSubmessage_n[:5])
        #[[('B', 1), ('D', 1), ('E', 1), ('F', 1), ('K', 1)],
        # [('I', 3), ('Z', 3), ('A', 2), ('E', 2), ('J', 2)],
        # [('C', 3), ('G', 2), ('H', 2), ('I', 2), ('M', 2)],
        # [('K', 2), ('N', 2), ('R', 2), ('V', 2), ('Y', 2)]]

    print(allFrequencyScores)

    # II etap: zostawmy tylko litery z najwyższym wynikiem dopasowania
    for i in range(len(allFrequencyScores)):
        scores = [tuple[1] for tuple in allFrequencyScores[i]]
        maxScoresOnly = [t for t in allFrequencyScores[i] if t[1] == max(scores)]
        allFrequencyScores[i] = maxScoresOnly

    #print(allFrequencyScores)
    #[[('B', 1), ('D', 1), ('E', 1), ('F', 1), ('K', 1)],
    # [('I', 3), ('Z', 3)],
    # [('C', 3)],
    # [('K', 2), ('N', 2), ('R', 2), ('V', 2), ('Y', 2)]]

    potentialKeyLetters = []
    for list_ in allFrequencyScores:
        letterList = [t[0] for t in list_]
        potentialKeyLetters.append(letterList)

    #print(potentialKeyLetters)
    #[['B', 'D', 'E', 'F', 'K'], ['I', 'Z'], ['C'], ['K', 'N', 'R', 'V', 'Y']]

    #III etap: tworzymy iloczyny kartezjańskie => kombinacje możliwych kluczy
    possibleKeys = list(itertools.product(*potentialKeyLetters))

    for possibleKey in possibleKeys:
        key = ''.join(possibleKey)
        print(key)
        keyReplication = vigenere.generateKeyReplication(testMsg, key)
        decryptedText = vigenere.decrypt(testMsg, keyReplication)
        #print(decryptedText)


    #[('B', 'I', 'C', 'K'), ('B', 'I', 'C', 'N'), ('B', 'I', 'C', 'R'),('B', 'I','C', 'V'), ('B', 'I', 'C', 'Y'), ('B', 'Z', 'C', 'K'),('B', 'Z', 'C', 'N'), ('B', 'Z', 'C', 'R'),…
    # i czas na próbę brute force'a na otrzymanej - niewielkiej - próbie możliwych kluczy
    #print(attemptCrackWithKeyLength(testMsg, 4))

if __name__ == '__main__':
    attemptCrackWithKeyLength(testMsg, 4)