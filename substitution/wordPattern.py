def getWordPattern(word: str):
    lettersList = list(word)
    cipher = 0
    ciphersList = [str(cipher)]

    for i in range(1, len(lettersList)):
        if word[i] not in lettersList[:i]:
            cipher += 1
            ciphersList.append(str(cipher))
        else:
            letterIndex = word.find(word[i])
            letterCipher = ciphersList[letterIndex]
            ciphersList.append(letterCipher)
    pattern = ''.join(ciphersList)
    return pattern

def loadDictionary(path: str):
    dictionaryFileObj = open(path)
    content = dictionaryFileObj.read()
    contentList = content.split('\n')
    englishWordsPatterns = {}
    for word in contentList:
        englishWordsPatterns[word] = getWordPattern(word)
    dictionaryFileObj.close()
    return englishWordsPatterns

ENGLISH_WORDS_PATTERNS = loadDictionary('../utils/files/dictionary.txt')

def getWordsFromPattern(pattern):
    words = list(filter(lambda k: ENGLISH_WORDS_PATTERNS[k] == pattern,
                        ENGLISH_WORDS_PATTERNS))
    return words

if __name__ == '__main__':
    word = "garden"
    pattern = getWordPattern(word)
    print(pattern)

    matches = getWordsFromPattern(pattern)
    print(matches)