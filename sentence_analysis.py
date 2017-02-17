import thesaurus

sentenceSubject = ''
sentenceVerb = ''
sentenceObject = ''


def analyze(userInput, subject, sentVerb, sentObject):
    sentence = userInput.split()
    for word in sentence:
        for noun in thesaurus.nouns:
            if word == noun and subject == '':
                subject = word
                break
        for verb in thesaurus.verbs:
            if word == verb and sentVerb == '':
                sentVerb = word
                break
        for thing in thesaurus.nouns:
            if word == thing and sentObject == '':
                sentObject = word
                break
    identifyConnotation(userInput)


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
