import datetime

class Library:
    def __init__(self):
        self.__books = {
            "Python Programming": 3,
            "Data Structures": 2,
            "Machine Learning": 4,
            "Artificial Intelligence": 5
        }
        self.__borrowed_books = {}

    def display_books(self):
        print("\nAvailable Books:")
        for book, quantity in self.__books.items():
            print(f"- {book} ({quantity} available)")

    def is_available(self, book_name):
        return self.__books.get(book_name, 0) > 0

    def borrow_book(self, book_name, user):
        if self.is_available(book_name):
            self.__books[book_name] -= 1
            borrow_info = {"book": book_name, "date": datetime.date.today()}
            self.__borrowed_books.setdefault(user, []).append(borrow_info)
            print(f"\n{user} has borrowed '{book_name}' on {borrow_info['date']}. Return within 7 days.")
        else:
            print("\nSorry, this book is not available right now.")

    def return_book(self, user, book_name):
        found = False
        if user in self.__borrowed_books:
            for i, borrow in enumerate(self.__borrowed_books[user]):
                if borrow["book"] == book_name:
                    found = True
                    borrow_date = borrow["date"]
                    return_date = datetime.date.today()
                    days_borrowed = (return_date - borrow_date).days
                    fine = 0
                    if days_borrowed > 7:
                        fine = (days_borrowed - 7) * 10
                    del self.__borrowed_books[user][i]
                    if not self.__borrowed_books[user]:
                        del self.__borrowed_books[user]
                    self.__books[book_name] += 1
                    print(f"\n{user} returned '{book_name}' on {return_date} (Borrowed: {borrow_date}).")
                    if fine > 0:
                        print(f"Late by {days_borrowed - 7} days. Fine: Rs. {fine}")
                    else:
                        print("Returned on time. No fine.")
                    break
        if not found:
            print("\nNo record found for this book and user.")

    def add_book(self, book_name, quantity):
        self.__books[book_name] = self.__books.get(book_name, 0) + quantity
        print(f"\n{quantity} copies of '{book_name}' added successfully!")

    def remove_book(self, book_name):
        if book_name in self.__books:
            del self.__books[book_name]
            print(f"\n'{book_name}' removed from library!")
        else:
            print("\nBook not found!")

class User(Library):
    def __init__(self):
        super().__init__()

    def user_menu(self):
        name = input("\nEnter your name: ")
        while True:
            print("\nUser Menu")
            print("1. View Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_books()
            elif choice == "2":
                book = input("Enter book name: ")
                self.borrow_book(book, name)
            elif choice == "3":
                book = input("Enter book name to return: ")
                self.return_book(name, book)
            elif choice == "4":
                print("\nLogging out...")
                break
            else:
                print("Invalid choice! Try again.")

class Librarian(User):
    __librarians = {
        "admin": "admin123",
        "librarian1": "pass123"
    }

    def __init__(self):
        super().__init__()

    @staticmethod
    def login():
        username = input("Enter librarian username: ")
        password = input("Enter librarian password: ")
        if Librarian.__librarians.get(username) == password:
            print("\nLogin successful!")
            return True
        else:
            print("\nIncorrect username or password!")
            return False

    def librarian_menu(self):
        while True:
            print("\nLibrarian Menu")
            print("1. View Books")
            print("2. Add Book")
            print("3. Remove Book")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_books()
            elif choice == "2":
                book = input("Enter book name: ")
                try:
                    quantity = int(input("Enter number of copies: "))
                    self.add_book(book, quantity)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "3":
                book = input("Enter book name: ")
                self.remove_book(book)
            elif choice == "4":
                print("\nLogging out...")
                break
            else:
                print("Invalid choice! Try again.")

def main():
    while True:
        print("\n==== Library Management System ====")
        print("1. User Login")
        print("2. Librarian Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user = User()  
            user.user_menu()
        elif choice == "2":
            if Librarian.login():
                librarian = Librarian()
                librarian.librarian_menu()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

main()
