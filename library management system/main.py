# This script demonstrates how to use the library management system.
from library_management.library import Library

def main():
    library = Library()

    # Add books to the library
    print(library.add_book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3))
    print(library.add_book("9780061120084", "To Kill a Mockingbird", "Harper Lee", 1960, 5))

    # Add users to the library
    print(library.add_user("u001", "Alice"))
    print(library.add_user("u002", "Bob"))

    # Borrow books
    print(library.borrow_book("u001", "9780743273565"))
    print(library.borrow_book("u002", "9780743273565"))

    # List all books
    books = library.list_books()
    if books:
        for book in books:
            print(book)

    # Return books
    print(library.return_book("u001", "9780743273565"))
    print(library.return_book("u002", "9780743273565"))

    # List all books after return
    books = library.list_books()
    if books:
        for book in books:
            print(book)

if __name__ == "__main__":
    main()
