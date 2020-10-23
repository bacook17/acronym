import numpy as np
import re

regex = re.compile('[^a-zA-Z]')


def score_word(word):
    word = regex.sub('', word)  # leave only alpha
    score = len(word)
    if (len(word) == 0) or word.islower():
        return score
    if word[0].isupper():
        score += 5
    if len(word) == 1:
        return score
    if word[1].isupper():
        score += 2
    if len(word) == 2:
        return score
    if word[-1].isupper():
        score += 2
    return score

def score_acronym(capitalized_acronym):
    return sum([score_word(word) for word in capitalized_acronym.split(' ')])
