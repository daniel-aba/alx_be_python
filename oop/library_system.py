#!/usr/bin/env python3

"""
A module that demonstrates inheritance and composition for a library system.
It defines a base Book class, two derived classes (EBook, PrintBook), and
a Library class that manages a collection of books.
"""

class Book:
    """
    A base class to represent a generic book.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance with a title and author.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    A class representing an electronic book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance. Calls the base class constructor
        and adds a unique attribute for file size.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            file_size (int): The size of the electronic file in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a user-friendly string representation of the EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    A class representing a physical book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance. Calls the base class constructor
        and adds a unique attribute for page count.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The number of pages in the physical book.
        """
        super().__init__(title, author)
        self.page_count = page_count
        
    def __str__(self):
        """
        Returns a user-friendly string representation of the PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    A class that represents a library and uses composition to manage a collection of books.
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list to store books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book instance (Book, EBook, or PrintBook) to the library's collection.

        Args:
            book (Book): An instance of a book class.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book in the library.
        Polymorphism ensures the correct __str__ method is called for each book type.
        """
        for book in self.books:
            print(book)
