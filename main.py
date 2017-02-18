import math
import random
import thesaurus
import sentence_analysis





def keyStroke():
    key = str(input())
    return key


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
    userInput = str(input()).lower()