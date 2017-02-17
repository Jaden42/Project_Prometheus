import math
import random
import thesaurus
import sentence_analysis


# This will create a random greeting and bias that greeting so it is more likely to be used in the future.
def greeting():
    result = ""
    for phrase in thesaurus.greetings.keys():
        prob = random.randint(thesaurus.greetings[phrase], 10)
        if prob == 10:
            result = phrase
            break
    if result == "":
        greeting()
    elif result != "":
        if thesaurus.greetings[phrase] < 8:
            thesaurus.greetings[phrase] += 1
        return result


print(greeting())

while True:
    userInput = input().lower()
    sentence_analysis.analyze(userInput, sentence_analysis.sentenceSubject, sentence_analysis.sentenceVerb, sentence_analysis.sentenceObject)
