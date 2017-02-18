import math
import random
import thesaurus
import sentence_analysis


# This will choose a random word or phrase and bias that phrase so it is more likely to be used in the future.
def baisedspeech(dict):
    result = None
    for phrase in dict.keys():
        prob = random.randint(dict[phrase], 10)
        if prob == 10:
            result = phrase
            break
    if result is None:
        print('try again')
        baisedspeech(dict)
    else:
        if dict[result] < 8:
            dict[result] += 1
        print('got result')
        return result


print(baisedspeech(thesaurus.greetings))

while True:
    userInput = input().lower()
    print(sentence_analysis.findSubject(userInput))
    print(sentence_analysis.findVerb(userInput))
    print(sentence_analysis.findObject(userInput))
    print(sentence_analysis.identifyConnotation(userInput))