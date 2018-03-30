# ACRONYM (Acronym CReatiON for You and Me)
=====

A python-based tool for creating English-ish Acronyms from your long project name

To install, simply navigate to install directory, and run:
> make 

To use, run like the following:
> acronym.py "the long name of your very fancy project"

optional arguments:
  -h, --help            show this help message and exit
  --min-length MIN_LENGTH
                        minimum length acronym to generate (default: 3)
  --max-length MAX_LENGTH
                        maximum length acronym to generate (default: 6)
  --max-tries MAX_TRIES
                        maximum number of iterations to attempt (default:
                        100000)
  --first-weight FIRST_WEIGHT
                        factor to prefer first letters of each word (default:
                        10.0)
  --output OUTPUT       file to save results (default: STDOUT)
