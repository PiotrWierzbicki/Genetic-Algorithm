# Genetic-Algorithm
Genetic Algorithm wrote in Python 3.7, to determine the shortest route in real networks. It is heuristic method, so it is possible that algorithm won't determine best path.

Files:
- geneticAlgo.py - main file
- genes.py - file with genes class, contains the main logic
- randPaths.py - to determine random parents, who are needed in genes.py
- smallTopology.csv - network topology

To see how it work:
- run "geneticAlgo.py"
- choose first and last node

You can modify:
- number of iteration, to change number of generation 
- number of childs, to change number of childs in one generation
- mutation level(in percent), to change possibility of mutation
- network - it must be in the same folder, and must be '.csv' file
