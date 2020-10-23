# ACRONYM (Acronym CReatiON for You and Me)
=====

A python-based tool for creating English-ish Acronyms from your fancy project

`ACRONYM` is described in this paper released on the arXiv: https://arxiv.org/abs/1903.12180

`ACRONYM` can be installed using pip:

```
$ pip install acronym
```

Alternatively, you can clone this repository, navigate to the main directory, and run:
```
$ make install
```

To use, run like the following:
```
$ acronym "the long name of your very fancy project"
Collecting word corpus
Identifying matching acronyms
Process Complete
(Score) ACRONYM   : Spelling
============================================================
(   35) TELAMON   : ThE Long nAMe of yOur very faNcy project
(   35) THEOGAMY  : THE lOnG nAMe of your very fancY project
(   35) THEOGONY  : THE lOnG name of yOur very faNcY project
(   34) THEOMANCY : THE lOng naMe of your very fANCY project
(   32) TAVERT    : The long nAme of your VEry fancy pRojecT
(   32) TAREFA    : The long nAme of youR vEry FAncy project
(   31) TELERAN   : ThE Long namE of your veRy fANcy project
(   30) TELFER    : ThE Long name oF your vEry fancy pRoject
(   30) THENAR    : THE long Name of your very fAncy pRoject
(   30) TARPOT    : The long nAme of youR very fancy PrOjecT
(   30) THEREAT   : THE long name of youR vEry fAncy projecT
(   30) TORYFY    : The lOng name of youR verY FancY project
(   30) THREAP    : THe long name of youR vEry fAncy Project
(   30) TELARY    : ThE Long nAme of your veRy fancY project
(   30) THEAVE    : THE long nAme of your Very fancy projEct
(   30) TEAPOT    : ThE long nAme of your very fancy PrOjecT
(   29) THONGMAN  : THe lONG naMe of your very fANcy project
(   29) THERENCE  : THE long name of youR vEry faNCy projEct
(   28) TONNER    : The lONg Name of your vEry fancy pRoject
(   28) TENNER    : ThE loNg Name of your vEry fancy pRoject
(   28) TERVEE    : ThE long name of youR VEry fancy projEct
(   28) TAVERN    : The long nAme of your VERy faNcy project
(   28) TEEVEE    : ThE long namE of your VEry fancy projEct
(   28) TYRANT    : The long name of YouR very fANcy projecT
(   28) TELEUT    : ThE Long namE of yoUr very fancy projecT
(   28) TAUREAN   : The long nAme of yoUR vEry fANcy project
(   27) TAVER     : The long nAme of your VEry fancy pRoject
(   27) TEARER    : ThE long nAme of youR vEry fancy pRoject
(   27) TERRANCE  : ThE long name of youR veRy fANCy projEct
(   27) TAYER     : The long nAme of Your vEry fancy pRoject
```

Acronym Scoring System *New in Version 2.0.0*
```
For each capitalized letter in the acronym:
   * 10 points if first letter in a word (with exception of first letter)
   * 3 point if second or last letter in a word
   * 1 point otherwise
   * N bonus points if begins an N-length valid sub-word
       (ex: multiVariable -> 8 bonus points)
   * 2 bonus points if immediately following another capitalizd letter
```
optional arguments:
```
  -h, --help            show this help message and exit
  --min-length MIN_LENGTH
                        minimum length acronym to generate (default: 4)
  --max-length MAX_LENGTH
                        maximum length acronym to generate (default: 9)
  --max-results MAX_RESULTS
                        maximum number of options to generate (default: 30)
  --output OUTPUT       file to save results (prints to STDOUT if not given)
                        (default: STDOUT)
  --strict, -s          How strictly should the words be related to real
                        English? (-s for strict, -ss for very strict)
                        (default: None)
```
