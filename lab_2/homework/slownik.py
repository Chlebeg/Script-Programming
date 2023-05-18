import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################
slownik = {}

def zapisz():
    arguments = sys.argv[2:]
    numbers = []
    for argument in arguments:
        numbers = numbers + [*argument]
    numbers.sort()
    while numbers:
        number = numbers[0]
        counter = numbers.count(number)
        slownik[number] = counter
        numbers = numbers[counter:]


def wypisz():
    for x in slownik:
        print("{}: {},".format(x, slownik[x]), end=" ")
    print("", end="\n")

############################################
print('Załadowano moduł "{0}"'.format(__name__))
