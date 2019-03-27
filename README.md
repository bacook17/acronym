# ACRONYM (Acronym CReatiON for You and Me)
=====

A python-based tool for creating English-ish Acronyms from your fancy project

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
TAMOYO	The long nAMe of yOur very fancY prOject
TANREC	The long nAme of your very faNcy pRojECt
TAREFA	The long nAme of youR vEry FAncy project
TARPOT	The long nAme of youR very fancy PrOjecT
TAVERN	The long nAme of your VERy faNcy project
TAVERT	The long nAme of your VEry fancy pRojecT
[...]
```

optional arguments:
```
  --min-length MIN_LENGTH
                        minimum length acronym to generate (default: 4)
  --max-length MAX_LENGTH
                        maximum length acronym to generate (default: 6)
  --output OUTPUT       file to save results (default: STDOUT)
  --nested              whether to search for nested, known acronyms (default:
                        False)
  --strict, -s          How strictly should the words be related to real
                        English? (default: None)
```
