import math
import random
import thesaurus
import sentence_analysis


# This will create a random greeting and bias that greeting so it is more likely to be used in the future.
def baisedspeech(dict):
    result = None
    for phrase in dict.keys():
        prob = random.randint(dict[phrase], 10)
        if prob == 10:
            result = phrase
            break
    if result is None:
        baisedspeech(dict)
    elif result != "":
        if dict[result] < 8:
            dict[result] += 1
        return result


print(baisedspeech(thesaurus.greetings))

while True:
    userInput = input().lower()
    sentence_analysis.analyze(userInput, sentence_analysis.sentenceSubject, sentence_analysis.sentenceVerb, sentence_analysis.sentenceObject)
