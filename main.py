import math
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
    userInput = input().lower()
    print(sentence_analysis.findSubject(userInput))
    print(sentence_analysis.findVerb(userInput))
    print(sentence_analysis.findObject(userInput))
    print(sentence_analysis.identifyConnotation(userInput))