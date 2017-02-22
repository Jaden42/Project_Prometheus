import thesaurus

def analyzeSentence(userInput):
    sentence = userInput.split()
    SVO = sentence
    for word in sentence:
        if word in thesaurus.fillerWords:
            SVO.remove(word)
    for word in SVO:
        if word in thesaurus.questionWords:
            SVO.remove(word)
    return SVO


def identifyConnotation(userInput):
    connotation = ''
    localContValue = 0
    for word in userInput.split():
        if word in thesaurus.vocab.keys():
            localContValue += thesaurus.vocab[word]
    if localContValue > 2:
        connotation = 'positive'
    elif localContValue < -2:
        connotation = 'negative'
    else:
        connotation = 'neutral'
    return connotation
