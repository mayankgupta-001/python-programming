class Library:
    def __init__(self):
        self.books = {
            "Python Programming": 3,
            "Data Structures": 2,
            "Machine Learning": 4,
            "Artificial Intelligence": 5
        }
        self.borrowed_books = {}

    def display_books(self):
        print("\nAvailable Books:")
        for book, quantity in self.books.items():
            print(f"- {book} ({quantity} available)")

    def borrow_book(self, book_name, user):
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            self.borrowed_books[user] = book_name
            print(f"\n{user} has borrowed '{book_name}' successfully.")
        else:
            print("\nSorry, this book is not available right now.")

    def return_book(self, user):
        if user in self.borrowed_books:
            book_name = self.borrowed_books.pop(user)
            self.books[book_name] += 1
            print(f"\n{user} has returned '{book_name}'. Thank you!")
        else:
            print("\nNo record found for this user.")

    def add_book(self, book_name, quantity):
        if book_name in self.books:
            self.books[book_name] += quantity
        else:
            self.books[book_name] = quantity
        print(f"\n{quantity} copies of '{book_name}' added successfully!")

    def remove_book(self, book_name):
        if book_name in self.books:
            del self.books[book_name]
            print(f"\n'{book_name}' removed from library!")
        else:
            print("\nBook not found!")


librarians = {
    "admin": "admin123",
    "librarian1": "pass123"
}

def librarian_login():
    username = input("Enter librarian username: ")
    password = input("Enter librarian password: ")

    if username in librarians and librarians[username] == password:
        print("\nLogin successful!")
        return True
    else:
        print("\nIncorrect username or password! Access denied.")
        return False


library = Library()

while True:
    print("\nLibrary Management System")
    print("1. User Login")
    print("2. Librarian Login")
    print("3. Exit")

    role_choice = input("Enter your choice: ")

    if role_choice == "1": 
        while True:
            print("\nUser Menu")
            print("1. View Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Logout")

            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                library.display_books()
            elif user_choice == "2":
                name = input("Enter your name: ")
                book = input("Enter book name: ")
                library.borrow_book(book, name)
            elif user_choice == "3":
                name = input("Enter your name: ")
                library.return_book(name)
            elif user_choice == "4":
                print("\nLogging out...")
                break
            else:
                print("Invalid choice! Try again.")

    elif role_choice == "2": 
        if librarian_login():
            while True:
                print("\nLibrarian Menu")
                print("1. View Books")
                print("2. Add Book")
                print("3. Remove Book")
                print("4. Logout")

                lib_choice = input("Enter your choice: ")

                if lib_choice == "1":
                    library.display_books()
                elif lib_choice == "2":
                    book = input("Enter book name: ")
                    quantity = int(input("Enter number of copies: "))
                    library.add_book(book, quantity)
                elif lib_choice == "3":
                    book = input("Enter book name: ")
                    library.remove_book(book)
                elif lib_choice == "4":
                    print("\nLogging out...")
                    break
                else:
                    print("Invalid choice! Try again.")
        else:
            print("\nLogin failed!")

    elif role_choice == "3":
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")