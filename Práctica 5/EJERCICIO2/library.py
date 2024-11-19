# library.py
from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f"Book with ISBN {isbn} has been removed."
        return "Book not found."

    def borrow_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    return "Book is already borrowed."
                else:
                    book.is_borrowed = True
                    return f"Book {book.title} has been borrowed."
        return "Book not found."

    def return_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    return "Book was not borrowed."
                else:
                    book.is_borrowed = False
                    return f"Book {book.title} has been returned."
        return "Book not found."

    def search_by_title(self, title: str):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def search_by_author(self, author: str):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        return found_books

    def list_books(self):
        return [str(book) for book in self.books]

