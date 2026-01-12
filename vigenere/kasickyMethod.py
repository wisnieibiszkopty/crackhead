import re


def findSpacingsBetweenRepeatedSequences(message: str) -> dict[str, list[int]]:
    cleanMessage = re.sub(r'[^A-Z]', '', message.upper())
    messageLength = len(cleanMessage)
    sequences: dict[str, list[int]] = {}

    for sequenceLength in range(3, 5):
        for j in range(messageLength - sequenceLength + 1):
            seq = cleanMessage[j: j + sequenceLength]

            if seq not in sequences:
                sequences[seq] = []

            sequences[seq].append(j)

    sequencesSpacing: dict[str, list[int]] = {}

    for seq, indices in sequences.items():
        if len(indices) < 2:
            continue

        spacing = []
        for i in range(len(indices) - 1):
            spacing.append(indices[i + 1] - indices[i])

        sequencesSpacing[seq] = spacing

    return sequencesSpacing


def getFactors(number: int, maxKeyLength: int = 16) -> list[int]:
    factors = []
    for i in range(2, min(maxKeyLength, number) + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def getMostCommonFactor(sequencesSpacings: dict[str, list[int]]) ->list[tuple[int, int]]:
    sequencesFactors = {}
    for seq, spacings in sequencesSpacings.items():
        factorsList = []
        for spacing in spacings:
            factorsList.extend(getFactors(spacing))
        sequencesFactors[seq] = factorsList

    factorsCount = {}
    for factorsList in sequencesFactors.values():
        for factor in factorsList:
            factorsCount[factor] = factorsCount.get(factor, 0) + 1

    result = sorted(factorsCount.items(), key=lambda x: x[1], reverse=True)
    return result

def getKasickyExaminationResult(ciphertext: str):
    sequencesSpacings = findSpacingsBetweenRepeatedSequences(ciphertext)
    mostCommonFactors = getMostCommonFactor(sequencesSpacings)
    allLikelyKeyLengths = [factor for factor, count in mostCommonFactors]
    return allLikelyKeyLengths

if __name__ == '__main__':
    ciphertext = """jwetx osdafhuir dfgiorhk sdaith ldfuhioiosh se txoiht gdfse sda"""
    sequencesSpacings = findSpacingsBetweenRepeatedSequences(ciphertext)
    commonFactors = getMostCommonFactor(sequencesSpacings)

    print(sequencesSpacings)
    print(commonFactors)

    allLikelyKeyLengths = getKasickyExaminationResult(ciphertext)
    print(allLikelyKeyLengths)

    ciphertext = 'mHZWMwSA50CQZHV3CC1TYZZUAHROCR1B3T1JKDL8WTQSLZNwLA55IU5uSPNQXELoWNQIVYFwZHVF2TKMVYLQ1SL43EIE04CQLuuSMw,OSMQVAA5OCfNELgWTJu6QCVNELmQPMSLTOPOTVOCCAP9ZNQ1NUFQPZE9P1VAI5F2JKuWLVVGS\'FOGTRVFIPJu!W2KSA PT1AP9PKKVI L2GJuRYCC2A3LVENELZNwTE,FNCTTR47wHO6V1wGNUFIWZH631AAdYT1wNA0FTGJu ZCJOSL1WR1LR3CKJE55QHOCR5QQTuR4CVNEL"NCZHV3"wUFLXWFKR5FNCTTR47wRI PZCZU9PGw,ELT1w3IUPT1ARVRITJEUFIUAO5PCQLu SMwSO05CKTF36MPZIRWCC1TYZZUAOWFINRu TUGEu'
    sequencesSpacings = findSpacingsBetweenRepeatedSequences(ciphertext)
    commonFactors = getMostCommonFactor(sequencesSpacings)

    print(sequencesSpacings)
    print(commonFactors)

    allLikelyKeyLengths = getKasickyExaminationResult(ciphertext)
    print(allLikelyKeyLengths)

    ciphertext = 'PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'
    sequencesSpacings = findSpacingsBetweenRepeatedSequences(ciphertext)
    commonFactors = getMostCommonFactor(sequencesSpacings)

    print(sequencesSpacings)
    print(commonFactors)

    allLikelyKeyLengths = getKasickyExaminationResult(ciphertext)
    print(allLikelyKeyLengths)