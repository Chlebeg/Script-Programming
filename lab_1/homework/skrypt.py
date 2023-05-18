from math import sqrt, ceil


def is_prime(number):
    if number == 2 or number == 3:
        return True
    for i in range(2, ceil(sqrt(number) + 1)):
        if (number % i) == 0:
            return False
    return True


def script(data):
    arr = data.split(" ")
    for item in arr:
        if item.isdigit():
            item = int(item)
            if is_prime(item):
                print(item)


data = input()

script(data)
