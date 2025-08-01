class Book:
    """Represents a book in the library system."""
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        # Private attribute to track availability. Default to False (available).
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out if it's currently available.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available if it's currently checked out.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available (not checked out).

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book objects."""
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        # Private list to store Book objects.
        self._books = []

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added: {book.title}")
        else:
            print("Can only add Book objects to the library.")

    def check_out_book(self, title):
        """
        Checks out a book by its title if it's found and available.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.is_available(): # Check if available before attempting checkout
                    book.check_out()
                    print(f"Checked out: {title}")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        if not found:
            print(f"Error: Book '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Returns a book by its title if it's found and was checked out.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if not book.is_available(): # Check if checked out before attempting return
                    book.return_book()
                    print(f"Returned: {title}")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        if not found:
            print(f"Error: Book '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """
        Lists all books currently available in the library.
        """
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book) # Uses the __str__ method of the Book object
                available_count += 1
        if available_count == 0:
            print("No books currently available.")

