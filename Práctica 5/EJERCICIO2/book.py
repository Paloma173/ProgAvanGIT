# book.py

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_borrowed = False

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def is_borrowed(self) -> bool:
        return self._is_borrowed

    @is_borrowed.setter
    def is_borrowed(self, status: bool):
        self._is_borrowed = status

    def __str__(self) -> str:
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Borrowed: {self._is_borrowed}"

