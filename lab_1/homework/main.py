def sum(arg1, arg2):
    try:
        return complex(arg1) + complex(arg2)
    except TypeError:
        raise ValueError

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    print("suma =", sum(x, y))
    print("__name__ =", __name__)
else:
    print('Uruchamiamy z importu')
    print("__name__ =", __name__)
