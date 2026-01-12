class Book:
    def __init__(self, author, title = "unknown", isbn = "unknown", year = "unknown"):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = year

    def printBook(self):
        print(f"{self.author} {self.title} {self.isbn} {self.year}")

book1 = Book("Ola Kowalska", "Podróże", "3g234", 2020)
book1.printBook()

book2 = Book("Adam")
book2.printBook()