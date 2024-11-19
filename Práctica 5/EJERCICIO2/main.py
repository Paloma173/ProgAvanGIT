# main.py
from library import Library
from book import Book
from user import User
from utils import leer_int, crear_menu

def main():
    library = Library()
    users = []

    while True:
        print("\n--- Library Management System ---")
        options = [
            "Add book", "Remove book", "Register user", "Borrow book", 
            "Return book", "Show all books", "Search books by title", 
            "Search books by author", "Exit"
        ]
        choice = crear_menu(options)

        if choice == 1:  # Add book
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == 2:  # Remove book
            isbn = input("Enter book ISBN to remove: ")
            print(library.remove_book(isbn))

        elif choice == 3:  # Register user
            name = input("Enter user name: ")
            user = User(name)
            users.append(user)
            print(f"User {name} registered with ID {user.id}")

        elif choice == 4:  # Borrow book
            user_id = input("Enter user ID: ")
            user = next((u for u in users if u.id == user_id), None)
            if user:
                isbn = input("Enter book ISBN to borrow: ")
                print(library.borrow_book(isbn))
                if library.borrow_book(isbn) == "Book borrowed.":
                    book = next(b for b in library.books if b.isbn == isbn)
                    user.borrow_book(book)
            else:
                print("User not found.")

        elif choice == 5:  # Return book
            user_id = input("Enter user ID: ")
            user = next((u for u in users if u.id == user_id), None)
            if user:
                isbn = input("Enter book ISBN to return: ")
                book = next((b for b in user.borrowed_books if b.isbn == isbn), None)
                if book:
                    user.return_book(book)
                    print(library.return_book(isbn))
                else:
                    print("This book is not borrowed by the user.")
            else:
                print("User not found.")

        elif choice == 6:  # Show all books
            print("\n--- All Books ---")
            for book in library.list_books():
                print(book)

        elif choice == 7:  # Search books by title
            title = input("Enter book title to search: ")
            books = library.search_by_title(title)
            for book in books:
                print(book)

        elif choice == 8:  # Search books by author
            author = input("Enter author name to search: ")
            books = library.search_by_author(author)
            for book in books:
                print(book)

        elif choice == 9:  # Exit
            print("Exiting the library management system.")
            break

if __name__ == "__main__":
    main()
