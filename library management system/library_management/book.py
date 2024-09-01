class Book:
    def __init__(self, isbn, title, author, publication_year, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.total_copies = copies
        self.available_copies = copies

    def __repr__(self):
        return (f"Book(ISBN: '{self.isbn}', Title: '{self.title}', Author: '{self.author}', "
                f"Publication Year: {self.publication_year}, Available Copies: {self.available_copies})")

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
