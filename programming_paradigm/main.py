from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald")) # Added for more comprehensive testing

    # Initial list of available books
    print("\nAvailable books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\n--- Simulating Check Out ---")
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Try to check out an already checked out book
    print("\n--- Trying to Check Out '1984' again ---")
    library.check_out_book("1984")

    # Try to check out a non-existent book
    print("\n--- Trying to Check Out 'Moby Dick' ---")
    library.check_out_book("Moby Dick")

    # Simulate returning a book
    print("\n--- Simulating Return ---")
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

    # Try to return a book that was not checked out
    print("\n--- Trying to Return 'Brave New World' (not checked out) ---")
    library.return_book("Brave New World")

    # Try to return a non-existent book
    print("\n--- Trying to Return 'War and Peace' ---")
    library.return_book("War and Peace")


if __name__ == "__main__":
    main()