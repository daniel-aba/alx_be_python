#!/usr/bin/env python3

"""
A module that defines the Book class with magic methods.
"""

class Book:
    """
    The Book class models a book with a title, author, and publication year.
    It demonstrates the use of __init__, __del__, __str__, and __repr__ magic methods.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method.
        Prints a message when the Book object is about to be deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation method for a user-friendly output.
        Returns a formatted string like "Title by Author, published in Year".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation method for developers.
        Returns a string that can be used to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
