#! /usr/bin/env python
import numpy as np
from tqdm import trange
import re
import enchant
import argparse
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


def find_acronyms(s, min_length=3, max_length=6, first_weight=10.,
                  max_tries=10000):
    """
    Returns a dictionary of English acronyms from input string s
    
    Parameters
    ----------
    s : str
        input string name to find acronyms from
    min_length : int, optional
        minimum length acronym to generate, default is 3
    max_length : int, optional
        maximum length acronym to generate, default is 6
    first_weight : float, optional
        factor to prefer first letters of each word, default is 10.0
    max_tries : int, optional
        maximum number of random iterations to attempt, default is 10,000

    Returns
    -------
    results : dict
        Dictionary of results, where each key is an English acronym (all caps)
            and each value is the input string with acronym-letters capitalized
    """

    # Initialize dictionary and results
    d = enchant.Dict('en_US')
    results = dict()
    s = s.lower()

    weights = np.ones(len(s), dtype=float)
    # Never draw a space
    spaces = [space.start() for space in re.finditer(' ', s)]
    for i in spaces:
        weights[i] = 0.
    # How much to prefer first letters of each word
    first_letters = [0] + [i + 1 for i in spaces]
    for i in first_letters:
        weights[i] *= first_weight
    weights[0] = 0.  # algorithm always start with the first letter
    weights /= np.sum(weights)  # sum to 1
    # Always include the "generic" acronym in the results (ex: NASA)
    base_attempt = _get_acronym(s, first_letters)
    results[base_attempt] = _set_caps(s, first_letters)

    for _ in trange(max_tries, desc='Finding Acronyms'):
        # randomly draw a combination of letters
        n_letters = np.random.randint(low=min_length-1, high=max_length)
        idx = [0] + sorted(np.random.choice(np.arange(len(s)), size=n_letters,
                                            replace=False, p=weights))
        this_try = _get_acronym(s, idx)
        # check if is in the dictionary, and then add
        if (d.check(this_try.lower())) and (this_try not in results):
            results[this_try] = _set_caps(s, idx)
    return results


if __name__ == '__main__':
    # Setup the command-line tool
    formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=formatter)
    parser.add_argument('name', metavar='S', type=str,
                        help='the name to generate acronyms from')
    parser.add_argument('--min-length', default=3, type=int,
                        help='minimum length acronym to generate')
    parser.add_argument('--max-length', default=6, type=int,
                        help='maximum length acronym to generate')
    parser.add_argument('--max-tries', default=100000, type=int,
                        help='maximum number of iterations to attempt')
    parser.add_argument('--first-weight', default=10., type=float,
                        help='factor to prefer first letters of each word')
    parser.add_argument('--output', default='STDOUT', type=str,
                        help='file to save results')
    args = parser.parse_args()

    results = find_acronyms(args.name, min_length=args.min_length,
                            max_length=args.max_length,
                            max_tries=args.max_tries,
                            first_weight=args.first_weight)
    
    if args.output == 'STDOUT':
        f = sys.stdout
    else:
        f = open(args.output, 'w')
    for k in sorted(results.keys()):
        f.write('{:s}\t{:s}\n'.format(k, results[k]))
        f.flush()
    if args.output != 'STDOUT':
        f.close()
