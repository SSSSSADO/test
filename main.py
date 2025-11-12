class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

book = Book("My favourite book", 42)
print(1)
print(book.name)
print(book.author)