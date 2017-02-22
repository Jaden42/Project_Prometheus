import random
import thesaurus
import sentence_analysis


# This will choose a random word or phrase and bias that phrase so it is more likely to be used in the future.
def biasedspeech(dictionary):
    weightIndex = 0
    totalWeight = 0
    for n in dictionary.values():
        totalWeight += n
    choice = random.randint(1, totalWeight)
    for phrase in dictionary:
        weightIndex += dictionary[phrase]
        if weightIndex >= choice:
            dictionary[phrase] += 1
            return phrase


print(biasedspeech(thesaurus.greetings))

while True:
    # Take user input
    userInput = input().lower()

    # Initialize variables
    subject = ''
    verb = ''
    obj = ''

    # Identify parts of speech in the sentence
    for word in sentence_analysis.analyzeSentence(userInput):
        if word in thesaurus.nouns:
            subject = word
            break
    for word in sentence_analysis.analyzeSentence(userInput):
        if word in thesaurus.verbs:
            verb = word
            break
    for word in sentence_analysis.analyzeSentence(userInput):
        if word in thesaurus.nouns and word != subject:
            obj = word

    print(subject)
    print(verb)
    print(obj)

    print(sentence_analysis.identifyConnotation(userInput))