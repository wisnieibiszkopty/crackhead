def getWordPattern(word: str):
    word = word.upper()
    letters = {}
    result = []

    k = 0

    for symbol in word:
        if symbol not in letters:
            letters[symbol] = k
            k += 1
        result.append(letters[symbol])

    return tuple(result)

def loadDictionary(path: str):
    with open(path) as file:
        patterns = {}
        content = file.read()
        wordList = content.split('\n')

        for word in wordList:
            word = word.strip()
            if not word:
                continue

            pattern = getWordPattern(word)

            if pattern not in patterns:
                patterns[pattern] = []

            patterns[pattern].append(word)

        return patterns

def getWordsFromPattern(word: str, patterns):
    targetPattern = getWordPattern(word)

    if targetPattern in patterns:
        return patterns[targetPattern]
    else:
        return []

if __name__ == '__main__':
    word = "garden"
    print(getWordPattern(word))
    englishWordsPatterns = loadDictionary('../utils/files/dictionary.txt')

    matches = getWordsFromPattern(word, englishWordsPatterns)
    print(matches)