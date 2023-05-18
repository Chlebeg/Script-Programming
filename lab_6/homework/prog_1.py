from inspect import signature

last_not_used = 0

def arguments(operation_args):
    def inside(function):
        def findArgs(*args, **kwargs):
            needed_args = len(list(signature(function).parameters))
            ready_args = list(args)
            x = needed_args - len(ready_args)

            if x > len(operation_args):
                raise TypeError(f'{function.__name__} takes exactly {needed_args} arguments ({len(operation_args) + len(ready_args)} given)')

            global last_not_used
            last_not_used = operation_args[0]
            for y in range(0, x):
                ready_args.append(operation_args[y])
                if y < len(operation_args)-1:
                    last_not_used = operation_args[y+1]
                else:
                    last_not_used = 0

            return function(*ready_args)
        return findArgs
    return inside

class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    @arguments(argumentySuma)
    def suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')
        return a + b + c

    @arguments(argumentyRoznica)
    def roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')
        return x - y

    def u_suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')
        return a + b + c

    def u_roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')
        return x - y

    def update(self):
        self.suma = (arguments(self.argumentySuma))(self.u_suma)
        self.roznica = (arguments(self.argumentyRoznica))(self.u_roznica)

    def __setitem__(self, key, value):
        if key == 'suma':
            self.argumentySuma = value
        elif key == 'roznica':
            self.argumentyRoznica = value
        self.update()

    def __str__(self):
        return last_not_used


if __name__ == "__main__":
    op = Operacje()
    op.suma(1, 2, 3)  # Wypisze: 1+2+3=6
    op.suma(1, 2)  # Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.suma(1)  # Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
    # op.suma()  # TypeError: suma() takes exactly 3 arguments (2 given)
    op.roznica(2, 1)  # Wypisze: 2-1=1
    op.roznica(2)  # Wypisze: 2-4=-2
    wynik = op.roznica()  # Wypisze: 4-5=-1
    print(wynik)  # Wypisze: 6

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma'] = [1, 2]
    # oznacza, że   argumentySuma=[1,2]

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica'] = [1, 2, 3]
    # oznacza, że   argumentyRoznica=[1,2,3]