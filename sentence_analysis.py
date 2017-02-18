import thesaurus

sentenceSubject = ''
sentenceVerb = ''
sentenceObject = ''


def findSubject(userInput):
    sentence = userInput.split()
    subject = ''
    for word in sentence:
        for noun in thesaurus.nouns:
            if word == noun and subject == '':
                subject = word
                break
    return subject


def findVerb(userInput):
    sentVerb = ''
    for word in userInput.split():
        for verb in thesaurus.verbs:
            if word == verb and sentVerb == '':
                sentVerb = word
                break
    return sentVerb


def findObject(userInput):
    sentObject = ''
    for word in userInput.split():
        for thing in thesaurus.nouns:
            if word == thing and sentObject == '' and word != findSubject(userInput):
                sentObject = word
                break
    return sentObject


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
