from abc import ABC

class Book(ABC):
    id_counter = 1

    def __init__(self, author: str, title: str):
        self.id = Book.id_counter
        Book.id_counter += 1
        self.author = author
        self.title = title

    def __str__(self):
        return f'id:{self.id} - {self.author} - "{self.title}"'
