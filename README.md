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

*New in Version 2.0.2*

New option to add custom corpus, such as those in other languages (German,
Russian, ...) listed [here](https://wortschatz.uni-leipzig.de/en/download/).

```
  --corpus, -c          Path to the text file (words) to read in as corpus
                        (default: NULL)
```

```
acronym -c ~/Downloads/deu_news_2021_10K/deu_news_2021_10K-words.txt "Ich vermisse dich so sehr, aber du weißt es nicht, und ich kann nichts tun"
Collecting word corpus
Identifying matching acronyms
Process Complete
(Score) ACRONYM   : Spelling
==============================================================================================
(   45) INDIANS   : Ich vermisse dich so sehr, aber du weißt es Nicht, unD Ich kAnn NichtS tun
(   30) IDEEN     : Ich vermisse Dich so sEhr, aber du weißt Es nicht, und ich kann nichts tuN
(   30) INDIA     : Ich vermisse dich so sehr, aber du weißt es Nicht, unD Ich kAnn nichts tun
(   26) ISSUES    : Ich vermiSSe dich so sehr, aber dU weißt Es nicht, und ich kann nichtS tun
(   25) IDEE      : Ich vermisse Dich so sehr, aber du wEißt Es nicht, und ich kann nichts tun
(   25) IDRIS     : Ich vermisse Dich so sehR, aber du weißt es nicht, und ich kann nIchtS tun
(   25) IVES      : Ich Vermisse dich so sehr, aber du weißt Es nicht, und ich kann nichtS tun
(   25) INKA      : Ich vermisse dich so sehr, aber du weißt es Nicht, und ich KAnn nichts tun
(   23) IHRES     : IcH veRmisse dich so sehr, aber du weißt Es nicht, und ich kann nichtS tun
(   23) IRAK      : Ich veRmisse dich so sehr, Aber du weißt es nicht, und ich Kann nichts tun
(   23) IRWIN     : Ich veRmisse dich so sehr, aber du Weißt es nicht, und ich kann nIchts tuN
(   23) IHREN     : IcH veRmisse dich so sehr, aber du weißt Es nicht, und ich kann nichts tuN
(   23) IVICA     : Ich VermIsse dich so sehr, aber du weißt es nicht, und iCh kAnn nichts tun
(   23) IRRTE     : Ich veRmisse dich so sehR, aber du weißT Es nicht, und ich kann nichts tun
(   20) IWAN      : Ich vermisse dich so sehr, aber du Weißt es nicht, und ich kAnn nichts tuN
(   20) IHRE      : IcH vermisse dich so sehr, abeR du weißt Es nicht, und ich kann nichts tun
(   18) IRRE      : Ich veRmisse dich so sehr, abeR du weißt Es nicht, und ich kann nichts tun
(   18) ISAR      : Ich vermiSse dich so sehr, AbeR du weißt es nicht, und ich kann nichts tun
(   18) IMERI     : Ich verMissE dich so sehr, abeR du weißt es nicht, und ich kann nIchts tun
(   16) IRRER     : Ich veRmisse dich so sehR, abER du weißt es nicht, und ich kann nichts tun
(   16) IHRER     : IcH veRmisse dich so sehr, abER du weißt es nicht, und ich kann nichts tun
(   16) IRINA     : Ich veRmIsse dich so sehr, aber du weißt es nicht, uNd ich kAnn nichts tun
(   13) IRIS      : Ich veRmisse dich so sehr, aber du weißt es nicht, und ich kann nIchtS tun
(   13) IRAN      : Ich veRmisse dich so sehr, aber du weißt es nicht, und ich kAnn nichts tuN
(   13) ISIN      : Ich vermiSse dich so sehr, aber du weißt es nicht, und ich kann nIchts tuN
(   13) IUCN      : Ich vermisse dich so sehr, aber dU weißt es nicht, und ich kann niChts tuN
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
