from mylibrary.library import Library

def show_menu():
    print("\n📚 Library Menu:")
    print("1. Add book")
    print("2. Remove book")
    print("3. Search book")
    print("4. Show book")
    print("5. Exit")

if __name__ == "__main__":
    lib = Library()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            lib.add_book(title, author)
        elif choice == "2":
            lib.remove_book()
        elif choice == "3": 
            title = input("Enter book title to search: ")
            lib.search_book(title)
        elif choice == "4":
            lib.show_book()
        elif choice == "5":
            print("Exiting... 👋")
            break
        else:
            print("Invalid option. Try again.")