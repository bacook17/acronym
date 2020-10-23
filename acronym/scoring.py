import re

regex = re.compile('[^a-zA-Z]')


def score_word(word, corpus=None):
    word = regex.sub('', word)  # leave only alpha
    score = 0
    consec_bonus = 2
    for i, letter in enumerate(word):
        if letter.islower():
            continue
        if i > 0 and word[i-1].upper():
            score += consec_bonus
        if i == 0:
            score += 10
        elif (i == 1) or (i == len(word)-1):
            score += 3
        else:
            score += 1
        if (i >= 1) and (corpus is not None) and (word[i:].lower() in corpus):
            score += len(word[i:])-1
    return score


def score_acronym(capitalized_acronym, corpus=None):
    """
    For each capitalized letter in the acronym:
       * 10 points if first letter in a word (with exception of first letter)
       * 3 point if second or last letter in a word
       * 1 point otherwise
       * N bonus points if begins an N-length valid sub-word
            (ex: multiVariable -> 8 bonus points)
       * 2 bonus points if immediately following a capitalizd letter
    """
    return sum([score_word(word, corpus=corpus) for word in capitalized_acronym.split(' ')]) - 10
