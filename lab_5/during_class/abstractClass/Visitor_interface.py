from abc import ABC

class Visitor(ABC):
    def __init__(self, name: str, surname: str, pesel: int):
        self.name = name
        self.surname = surname
        self.pesel = pesel
        self.history = []

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        return f'{self.name} {self.surname} - pesel:{self.pesel} - history: {self.history}'