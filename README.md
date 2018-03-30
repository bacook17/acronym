# ACRONYM (Acronym CReatiON for You and Me)
=====

A python-based tool for creating English-ish Acronyms from your fancy project

To install, simply navigate to install directory, and run:
```
$ make 
```

To use, run like the following:
```
$ acronym.py "the long name of your very fancy project"
Finding Acronyms: 100%|███████████████████████████████████████████| 100000/100000 [00:23<00:00, 4177.39it/s]
TACT	The long name of your very fAnCy projecT
TAM	The long nAMe of your very fancy project
TAME	The long nAME of your very fancy project
TAMP	The long nAMe of your very fancy Project
TAN	The long name of your very fANcy project
TAO	The long nAme Of your very fancy project
[...]
```
optional arguments:
```
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
```
