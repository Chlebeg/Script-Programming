from functionalClass.BookForBuy_class import BookForBuy
from functionalClass.BookForBorrow_class import BookForBorrow
from functionalClass.Buyer_class import Buyer
from functionalClass.Borrower_class import Borrower

class Library:
    def __init__(self, bookFile, customerFile):
        self.bookDatabase = bookFile
        self.customerDatabase = customerFile
        self.myBooks = []
        self.myCustomers = []

    def findMyBook(self, id):
        for book in self.myBooks:
            if book.id == int(id):
                return book
        print("There is no book with this id: ", id)

    def findMyReader(self, pesel):
        for reader in self.myCustomers:
            if int(reader.pesel) == int(pesel):
                return reader
        print("There is no reader with this pesel: ", pesel)

    def parseBookDatabase(self):
        file = open(self.bookDatabase, "r")
        file_data = file.readlines()
        file.close()
        for line in file_data:
            args = line.split()
            if args[0] == "A":
                self.myBooks.append(BookForBuy(args[1], args[2], int(args[3]), int(args[4])))
            elif args[0] == "B":
                self.myBooks.append(BookForBorrow(args[1], args[2]))
            else:
                raise TypeError("Encountered problem in Book Database")

    def parseCustomerDatabase(self):
        file = open(self.customerDatabase, "r")
        file_data = file.readlines()
        file.close()
        for line in file_data:
            args = line.split()
            if args[0] == "A":
                self.myCustomers.append(Buyer(args[1], args[2], int(args[3])))
            elif args[0] == "B":
                self.myCustomers.append(Borrower(args[1], args[2], int(args[3])))
            else:
                raise TypeError("Encountered problem in Customer Database")

    def parseBothDatabases(self):
        self.parseBookDatabase()
        self.parseCustomerDatabase()

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
            if isinstance(reader, Buyer):
                print("You cannot return bought books")
                return
            return reader - book
        else:
            print("Wrong action")

    def __str__(self):
        return f'Readers:\n{self.myCustomers}\nMy books:\n{self.myBooks}'
