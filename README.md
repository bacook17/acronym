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
                        minimum length acronym to generate (default: 3)
  --max-length MAX_LENGTH
                        maximum length acronym to generate (default: 6)
  --output OUTPUT       file to save results (default: STDOUT)
  --nested              whether to search for nested, known acronyms (default:
                        False)
```
