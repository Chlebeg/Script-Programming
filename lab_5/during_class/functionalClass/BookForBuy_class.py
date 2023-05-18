from abstractClass.Book_abstract import Book

class BookForBuy(Book):
    def __init__(self, author: str, title: str, price: int, amount: int):
        super().__init__(author, title)
        self.price = price
        self.amount = amount
        self.sold = 0

    def __repr__(self):
        return f'id:{self.id} {self.author} "{self.title}", still have:{self.amount} sold:{self.sold} - earned {self.sold*self.price}'
