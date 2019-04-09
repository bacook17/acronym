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
TERRACE	ThE long name of youR veRy fAnCy projEct
THEREAT	THE long name of youR vEry fAncy projecT
TYRRANY	The long name of YouR veRy fANcY project
TAVERN	The long nAme of your VERy faNcy project
TEAPOT	ThE long nAme of your very fancy PrOjecT
TENANT	ThE loNg name of your very fANcy projecT
TENOUR	ThE loNg name of yOUr very fancy pRoject
TENURE	ThE loNg name of yoUr very fancy pRojEct
[...]
```

optional arguments:
```
  --min-length MIN_LENGTH
                        minimum length acronym to generate (default: 4)
  --max-length MAX_LENGTH
                        maximum length acronym to generate (default: 8)
  --output OUTPUT       file to save results (default: STDOUT)
  --nested              whether to search for nested, known acronyms (default:
                        False)
  --strict, -s          How strictly should the words be related to real
                        English? (default: None)
```
