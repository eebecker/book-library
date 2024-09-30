# main.py

from book_manager import BookManager

def display_menu():
    """Display the menu options to the admin."""
    print("\nMenu:")
    print("1. Add a new book")
    print("2. Remove a book by title")
    print("3. List all books")
    print("4. Exit the program")

def main():
    """Main function to run the program."""
    book_manager = BookManager('books.txt')

    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")
            try:
                year = int(year)
                book_manager.add_book(title, author, year)
            except ValueError:
                print("Please enter a valid year.")

        elif choice == '2':
            title = input("Enter book title to remove: ")
            book_manager.remove_book(title)

        elif choice == '3':
            book_manager.list_books()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
