# user.py
import uuid

class User:
    def __init__(self, name: str):
        self._name = name
        self._id = str(uuid.uuid4())[:8]  # Unique user ID
        self._borrowed_books = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> str:
        return self._id

    @property
    def borrowed_books(self) -> list:
        return self._borrowed_books

    def borrow_book(self, book):
        self._borrowed_books.append(book)

    def return_book(self, book):
        self._borrowed_books.remove(book)

    def __str__(self) -> str:
        borrowed_titles = [book.title for book in self._borrowed_books]
        return f"User: {self._name}, ID: {self._id}, Borrowed books: {', '.join(borrowed_titles)}"
