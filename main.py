import math
import random
import thesaurus


# This will create a random greeting and bias that greeting so it is more likely to be used in the future.
def greeting():
    result = ""
    for phrase in thesaurus.greetings.keys():
        prob = random.randint(thesaurus.greetings[phrase], 10)
        if prob == 10:
            result = phrase
    if result == "":
        greeting()
    elif result != "":
        if thesaurus.greetings[phrase] < 8:
            thesaurus.greetings[phrase] += 1
        return result


print(greeting())
print(thesaurus.greetings)
