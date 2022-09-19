#! /usr/bin/env python

__version__ = '2.0.2'

import os
import numpy as np
import pandas as pd
import re
# import enchant
import nltk
from nltk.corpus import PlaintextCorpusReader
from .scoring import score_acronym
try:
    nltk.corpus.words.ensure_loaded()
    nltk.corpus.brown.ensure_loaded()
    nltk.corpus.gutenberg.ensure_loaded()
except LookupError:
    print('Initial downloading of word corpus')
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    for d in ['words', 'brown', 'gutenberg']:
        nltk.download(d)
import argparse
import textwrap
import sys


__all__ = ['find_acronyms']


def _set_caps(s, idx):
    """
    Returns a version of input string s, where letters given by indices idx
    are capitalized, and all others are lower-case
    """
    result = ''
    s = s.lower()
    for i in range(len(s)):
        if i in idx:
            result += s[i].upper()
        else:
            result += s[i]
    return result


def _get_acronym(s, idx):
    """
    Returns only the letters of input string s given by indices idx
    (results are ALL CAPS)
    """
    result = ''
    for i in idx:
        if i > len(s):
            continue
        result += s[i].upper()
    return result


def _index_in(s, word, offset=0, must_start=False):
    """
    Returns a list of indices for each character of word (in order) in s
    If word cannot be found in-order within s, returns None
    If multiple possibilities, returns only one possible solution
    
    The algorithm is recursive, and offset and must_start are used
    for later iterations of the algorithm.
    """
    if must_start and not s.startswith(word[0]):
        return None
    # Base case
    if len(word) == 1:
        if word in s:
            return [s.find(word) + offset]
        else:
            return None
    # Use regular-expressions to search for any substring starting and ending
    # with first and last letters of "word"
    pattern = word[0] + '\D*' + word[-1]
    result = re.search(pattern, s)
    if result is None:
        return None
    start = result.start()
    end = result.end() - 1
    # If these were last two letters of word
    if len(word) == 2:
        return [start+offset, end+offset]
    # recursively search interior of substring
    else:
        sub_s = s[start+1:end]
        sub_word = word[1:-1]
        sub_result = _index_in(sub_s, sub_word, offset=start+offset+1,
                               must_start=False)
        if sub_result is None:
            return None
        else:
            return [start + offset] + sub_result + [end + offset]


def find_acronyms(s, corpus, min_length=5, max_length=7):
    """
    Returns a dictionary of English acronyms from input string s
    
    Parameters
    ----------
    s : str
        input string name to find acronyms from
    corpus : nltk corpus object
        which corpus of words to use for reference
    min_length : int, optional
        minimum length acronym to generate, default is 5
    max_length : int, optional
        maximum length acronym to generate, default is 7

    Returns
    -------
    results : dict
        Dictionary of results, where each key is an English acronym (all caps)
            and each value is the input string with acronym-letters capitalized
    """

    # Initialize dictionary and results
    results = dict()
    scores = dict()
    s = s.lower()
    first = s[0]
    print('Collecting word corpus')
    full_list = corpus.words()
    short_list = np.unique([w.lower() for w in full_list if 3 <= len(w)
                            and w.isalpha()])
    word_list = np.unique([w.lower() for w in full_list if min_length <= len(w)
                           and len(w) <= max_length
                           and w.lower().startswith(first)
                           and w.isalpha()])
    print('Identifying matching acronyms')
    for word in word_list:
        if word.lower() in s:
            continue
        result = _index_in(s, word, must_start=True)
        if result is not None:
            acronym = word.upper()
            cap_version = _set_caps(s, result)
            results[acronym] = cap_version
            scores[acronym] = score_acronym(cap_version, corpus=short_list)
    print('Process Complete')
    results = pd.DataFrame({'long_version': results,
                            'score': scores})
    results.index.name = 'acronym'
    return results.sort_values('score', ascending=False)

def validate_file(f):
    if f != 'NULL' and not os.path.exists(f):
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f

def main():
    # Setup the command-line tool
    formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(
        prog="acronym",
        formatter_class=formatter,
        epilog=(
            textwrap.dedent("Scoring System:\n"+score_acronym.__doc__)
        ),
    )
    parser.add_argument('name', metavar='ProjectName', type=str,
                        help='the name to generate acronyms from')
    parser.add_argument('--min-length', default=4, type=int,
                        help='minimum length acronym to generate')
    parser.add_argument('--max-length', default=9, type=int,
                        help='maximum length acronym to generate')
    parser.add_argument('--max-results', default=30, type=int,
                        help='maximum number of options to generate')
    parser.add_argument('--output', default='STDOUT', type=str,
                        help='file to save results (prints to STDOUT if not given)')
    parser.add_argument('--strict', '-s', action='count',
                        help='How strictly should the words be related to real English? (-s for strict, -ss for very strict)')
    parser.add_argument('--corpus', '-c', default="NULL", type=validate_file,
                        help='Absolute path to the .txt file to read in as corpus. Overwrite the strict option')

    parser.add_argument('--version', action='version', version='%(prog)s' + f'{__version__}')
    args = parser.parse_args()

    if args.strict in [0, None]:
        corpus = nltk.corpus.words
    elif args.strict == 1:
        corpus = nltk.corpus.brown
    else:
        corpus = nltk.corpus.gutenberg
    
    if args.corpus != 'NULL':
        corpus_root = os.path.dirname(args.corpus)
        corpus_file = os.path.basename(args.corpus)
        corpus = PlaintextCorpusReader(corpus_root, corpus_file)

    results = find_acronyms(args.name, corpus,
                            min_length=args.min_length,
                            max_length=args.max_length)
    
    if args.output == 'STDOUT':
        f = sys.stdout
    else:
        f = open(args.output, 'w')
    f.write(f'(Score) {"ACRONYM":{args.max_length+1}s}: Spelling\n')
    f.write('='*(len(args.name)+args.max_length+11)+'\n')
    for i, (key, row) in enumerate(results.sort_values('score', ascending=False).iterrows()):
        if i >= args.max_results:
            break
        f.write(f'({row.score:5d}) {key:{args.max_length+1}s}: {row.long_version:s}\n')
        f.flush()
    if args.output != 'STDOUT':
        f.close()


if __name__ == '__main__':
    main()

    
