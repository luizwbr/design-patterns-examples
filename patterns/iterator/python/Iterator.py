from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

# Iterator interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

# Book
@dataclass
class Book:
    title: str
    author: str

# Concrete Iterator
class BookIterator(Iterator):
    def __init__(self, books: List[Book]):
        self._books = books
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._books)

    def next(self) -> Book:
        if self.has_next():
            book = self._books[self._index]
            self._index += 1
            return book
        return None

# Concrete Collection
class BookCollection:
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book):
        self._books.append(book)

    def create_iterator(self) -> Iterator:
        return BookIterator(self._books)


if __name__ == "__main__":
    collection = BookCollection()
    collection.add_book(Book("Design Patterns", "Gang of Four"))
    collection.add_book(Book("Clean Code", "Robert Martin"))
    collection.add_book(Book("The Pragmatic Programmer", "Hunt & Thomas"))

    iterator = collection.create_iterator()
    print("Books in collection:")
    while iterator.has_next():
        book = iterator.next()
        print(f"- {book.title} by {book.author}")
