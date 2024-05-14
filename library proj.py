class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # 'student' or 'librarian'

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
        self.borrower = None

class Library:
    def __init__(self):
        self.users = {}
        self.books = [
            Book("Book1", "Author1"),
            Book("Book2", "Author2"),
            Book("Book3", "Author3"),
            Book("Book4", "Author4"),
            Book("Book5", "Author5"),
        ]
        self.current_user = None

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (student/librarian): ")
        if role not in ['student', 'librarian']:
            print("Invalid role. Please enter 'student' or 'librarian'.")
            return
        for user in self.users.values():
            if user.username == username and user.password == password:
                print("Username and password already exist.")
                return
        if username and password in self.users:
            print("Username already exists. Please choose another one.")
        else:
            self.users[username] = User(username, password, role)
            print("Registration successful!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users and self.users[username].password == password:
            print("Login successful!")
            self.current_user = self.users[username]
        else:
            print("Invalid username or password.")

    def view_books(self):
        if self.books:
            print("Available Books:")
            for book in self.books:
                if book.available:
                    print(f"{book.title} by {book.author}")
        else:
            print("No books available in the library.")

    def borrow_book(self):
        book_title = input("Enter the title of the book you want to borrow: ")
        for book in self.books:
            if book.title == book_title and book.available:
                book.available = False
                book.borrower = self.current_user.username
                print(f"{book_title} borrowed successfully by {self.current_user.username}.")
                return
        print("Book not available.")

    def return_book(self):
        book_title = input("Enter the title of the book you want to return: ")
        for book in self.books:
            if book.title == book_title and not book.available:
                book.available = True
                print(f"{book_title} returned successfully by {self.current_user.username}.")
                return
        print("Invalid book title or book already returned.")

    def add_book(self):
        if self.current_user.role != 'librarian':
            print("Only librarian can add books.")
            return
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        self.books.append(Book(title, author))
        print("Book added successfully.")

    def remove_book(self):
        if self.current_user.role != 'librarian':
            print("Only librarian can remove books.")
            return
        title = input("Enter the title of the book you want to remove: ")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{title} removed successfully.")
                return
        print("Book not found.")

    def view_borrowed_books(self):
        if self.current_user.role != 'librarian':
            print("Only librarian can view borrowed books.")
            return
        borrowed_books = [book for book in self.books if not book.available]
        if borrowed_books:
            print("Borrowed Books:")
            for book in borrowed_books:
                print(f"{book.title} is borrowed by {book.borrower}")
        else:
            print("No books are currently borrowed.")

    def logout(self):
        self.current_user = None
        print("Logged out successfully!")

# Sample usage:
library = Library()

while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. View Books")
    print("4. Borrow Book")
    print("5. Return Book")
    if library.current_user and library.current_user.role == 'librarian':
        print("6. Add Book")
        print("7. Remove Book")
        print("8. View Borrowed Books")
    print("9. Log out")
    print("10. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        library.register_user()
    elif choice == '2':
        library.login()
    elif choice == '3':
        library.view_books()
    elif choice == '4':
        if library.current_user:
            library.borrow_book()
        else:
            print("Please log in first.")
    elif choice == '5':
        if library.current_user:
            library.return_book()
        else:
            print("Please log in first.")
    elif choice == '6':
        if library.current_user and library.current_user.role == 'librarian':
            library.add_book()
        else:
            print("Only librarian can add books.")
    elif choice == '7':
        if library.current_user and library.current_user.role == 'librarian':
            library.remove_book()
        else:
            print("Only librarian can remove books.")
    elif choice == '8':
        library.view_borrowed_books()
    elif choice == '9':
        library.logout()
    elif choice == '10':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
