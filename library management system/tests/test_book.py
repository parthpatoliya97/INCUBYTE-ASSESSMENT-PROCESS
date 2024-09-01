import unittest
from library_management.book import Book

class TestBook(unittest.TestCase):

    def test_book_initialization(self):
        book = Book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
        self.assertEqual(book.isbn, "9780743273565")
        self.assertEqual(book.title, "The Great Gatsby")
        self.assertEqual(book.author, "F. Scott Fitzgerald")
        self.assertEqual(book.publication_year, 1925)
        self.assertEqual(book.total_copies, 3)
        self.assertEqual(book.available_copies, 3)

    def test_borrow_book(self):
        book = Book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
        self.assertTrue(book.borrow())
        self.assertEqual(book.available_copies, 2)

    def test_return_book(self):
        book = Book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
        book.borrow()
        book.return_book()
        self.assertEqual(book.available_copies, 3)

if __name__ == '__main__':
    unittest.main()
