import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################
lista = []

def zapisz():
    arguments = sys.argv[2:]
    numbers = []
    for argument in arguments:
        numbers = numbers + [*argument]
    numbers.sort()
    while numbers:
        number = numbers[0]
        counter = numbers.count(number)
        lista.append(number)
        lista.append(counter)
        numbers = numbers[counter:]


def wypisz():
    for x in range(len(lista)//2):
        print("{}: {},".format(lista[2 * x], lista[2 * x + 1]), end=" ")
    print("",end="\n")

############################################
print('Załadowano moduł "{0}"'.format(__name__))
