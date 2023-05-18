from Book_class import Book
from Reader_class import Reader

# myBooks = [Book, Book]

class Library():
    def __init__(self, fileName):
        self.fileName = fileName
        self.myBooks: list[Book] = []
        self.myReaders: list[Reader] = [Reader("Bomek", "Tojdys", "1"), Reader("Wacia", "Macia", "2")]

    def findMyBook(self, id):
        for book in self.myBooks:
            if book.id == int(id):
                return book
        print("There is no book with this id: ", id)

    def findMyReader(self, pesel):
        for reader in self.myReaders:
            if int(reader.pesel) == int(pesel):
                return reader
        print("There is no reader with this pesel: ", pesel)

    def parseFileLine(self):
        # input as [author, title]
        file = open(self.fileName, "r")
        file_data = file.readlines()
        file.close()
        for line in file_data:
            args = line.split()
            self.myBooks.append(Book(args[0], args[1]))

    def parseInputLine(self, request):
        action = request.split()
        pesel = action[0]
        operation = action[1]
        id = action[2]

        book = self.findMyBook(id)
        if not book:
            return

        reader = self.findMyReader(pesel)
        if not reader:
            return

        if operation == "+":
            return reader + book
        elif operation == "-":
            return reader - book
        else:
            print("Wrong action")

    def __str__(self):
        return f'Readers:\n{self.myReaders}\nMy books:\n{self.myBooks}'
