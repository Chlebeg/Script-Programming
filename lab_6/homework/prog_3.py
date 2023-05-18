import sys
import functools
print(len(list(filter(lambda n: int(n) % 2 == 0, functools.reduce(lambda x, y : x + y, [open(file, 'r').read().split() for file in sys.argv[1:]])))))
# python .\prog_3.py plik1.txt plik2.txt
