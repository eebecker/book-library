# book_manager.py
from difflib import SequenceMatcher

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class BookManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Load books from the text file."""
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    title, author, year = line.strip().split(',')
                    self.books.append(Book(title, author, int(year)))
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty inventory.")
        except Exception as e:
            print(f"Error loading books: {e}")

    def save_books(self):
        """Save books to the text file."""
        with open(self.filename, 'w') as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.year}\n")

    def add_book(self, title: str, author: str, year: int):
        """Add a new book to the inventory."""
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Added: {new_book}")

    def remove_book(self, title: str):
        """Remove a book from the inventory by its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print(f"Removed: {book}")
                return
            elif SequenceMatcher(None, book.title.lower(),title.lower()).ratio() > 0.7:
                print(f"Do you meant to say '{book.title}'")
                answer = input("Yes or No? ")
                if answer.lower() == 'yes':
                    self.books.remove(book)
                    self.save_books()
                    print(f"Removed: {book}")
                    return
                else:
                    return
        print("Book not found")            

    def list_books(self):
        """List all books in the inventory."""
        if not self.books:
            print("No books in inventory.")
        else:
            print("Books in Inventory:")
            for book in self.books:
                print(book)

    def search_book(self, title: str):
        """Search for a book by title."""
        for book in self.books:
            if book.title == title:
                print(f"Found: {book}")
                return
        print(f"Book titled '{title}' not found.")
