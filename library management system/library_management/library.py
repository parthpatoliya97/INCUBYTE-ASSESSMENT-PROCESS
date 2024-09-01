from .book import Book
from .user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, isbn, title, author, publication_year, copies):
        if not any(book.isbn == isbn for book in self.books):
            book = Book(isbn, title, author, publication_year, copies)
            self.books.append(book)
            return f"Book '{title}' added to the library."
        return "Book with this ISBN already exists."

    def list_books(self):
        return self.books if self.books else None

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)
            return f"User '{name}' added to the library."
        return "User ID already exists."

    def borrow_book(self, user_id, isbn):
        user = self.users.get(user_id)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if user and book:
            if user.borrow_book(book):
                return f"Book '{book.title}' borrowed successfully by {user.name}."
            else:
                return "No available copies to borrow."
        return "User or Book not found."

    def return_book(self, user_id, isbn):
        user = self.users.get(user_id)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if user and book:
            if user.return_book(book):
                return f"Book '{book.title}' returned successfully by {user.name}."
            else:
                return "Book not found in user's borrowed list."
        return "User or Book not found."
