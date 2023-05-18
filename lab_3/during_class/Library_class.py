class Library():
    def __init__(self, fileName):
        self.fileName = fileName
        self.myBooks = {}
        self.borrowedBooks = {}

    def borrow(self, request):
        who = request[0]
        bookname = request[1]
        quantity = int(request[2])
        if self.myBooks.keys().__contains__(bookname):
            if self.myBooks[bookname] >= quantity:
                if self.borrowedBooks.keys().__contains__(who):
                    if self.borrowedBooks[who].keys().__contains__(bookname):
                        self.borrowedBooks[who][bookname] += quantity
                    else:
                        self.borrowedBooks[who][bookname] = quantity
                else:
                    self.borrowedBooks[who] = {bookname: quantity}
                self.myBooks[bookname] -= quantity
            else:
                print("We don't have enough books")
                return False
        else:
            print("We don't have that type of book")
            return False

    def give_back(self, request):
        who = request[0]
        bookname = request[1]
        quantity = int(request[2])
        if self.borrowedBooks.keys().__contains__(who):
            if self.borrowedBooks[who].keys().__contains__(bookname):
                self.borrowedBooks[who][bookname] -= quantity
            else:
                self.borrowedBooks[who][bookname] = -quantity
        else:
            self.borrowedBooks[who] = {bookname: -quantity}
        if self.myBooks.keys().__contains__(bookname):
            self.myBooks[bookname] += quantity
        else:
            self.myBooks[bookname] = quantity

    def parseFileLine(self):
        file = open(self.fileName, "r")
        file_data = file.readlines()
        file.close()
        for line in file_data:
            args = line.split()
            self.myBooks[args[0]] = int(args[1])
        return

    def parseInputLine(self, request):
        action = request.split()
        if action[0] == "borrow":
            self.borrow(action[1:])
        elif action[0] == "giveback":
            self.give_back(action[1:])
        else:
            print("Wrong action")
