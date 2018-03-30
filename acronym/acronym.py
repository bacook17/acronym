#! /usr/bin/env python
import numpy as np
from tqdm import trange
import re
import enchant
import argparse
import sys


__all__ = ['find_acronyms']


def _set_caps(s, idx):
    result = ''
    s = s.lower()
    for i in range(len(s)):
        if i in idx:
            result += s[i].upper()
        else:
            result += s[i]
    return result


def _get_acronym(s, idx):
    result = ''
    for i in idx:
        result += s[i].upper()
    return result


def find_acronyms(s, min_length=3, max_length=6, first_weight=10.,
                  max_tries=10000):
    d = enchant.Dict('en_US')
    results = dict()
    s = s.lower()

    weights = np.ones(len(s), dtype=float)
    # Never draw a space
    spaces = [space.start() for space in re.finditer(' ', s)]
    for i in spaces:
        weights[i] = 0.
    first_letters = [0] + [i + 1 for i in spaces]
    for i in first_letters:
        weights[i] *= first_weight
    weights[0] = 0.  # always start with the first letter
    weights /= np.sum(weights)  # sum to 1
    base_attempt = _get_acronym(s, first_letters)
    results[base_attempt] = _set_caps(s, first_letters)
    for _ in trange(max_tries, desc='Finding Acronyms'):
        n_letters = np.random.randint(low=min_length-1, high=max_length)
        idx = [0] + sorted(np.random.choice(np.arange(len(s)), size=n_letters,
                                            replace=False, p=weights))
        this_try = _get_acronym(s, idx)
        if (d.check(this_try.lower())) and (this_try not in results):
            results[this_try] = _set_caps(s, idx)
    return results


if __name__ == '__main__':
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
    parser.add_argument('--output', default=sys.stdout, type=str,
                        help='file to save results')
    args = parser.parse_args()

    results = find_acronyms(args.name, min_length=args.min_length,
                            max_length=args.max_length,
                            max_tries=args.max_tries,
                            first_weight=args.first_weight)
    
    if args.output is not sys.stdout:
        f = open(args.output, 'w')
    else:
        f = sys.stdout
    for k in sorted(results.keys()):
        f.write('{:s}\t{:s}\n'.format(k, results[k]))
        f.flush()
    if f is not sys.stdout:
        f.close()

