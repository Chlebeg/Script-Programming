import getopt
import sys

x, y = getopt.getopt(sys.argv[1:], "", ["modul="])

if x[0][1] == "lista":
    import lista
    lista.zapisz()
    lista.wypisz()
elif x[0][1] == "slownik":
    import slownik
    slownik.zapisz()
    slownik.wypisz()
