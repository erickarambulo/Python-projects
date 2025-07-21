# Project 1: Library Management System with Lists and Arrays

# Empty list for books
books = []

# Lets start with 1, and then keep adding + 1
book_id = 1

# Functions defined
def book_management():
    global book_id # Must add global to be able to access vriable book_id
    # Ask users to input something
    title = input("Please enter the title: ")
    author = input("Please enter the book author: ")
    genre = input("Please enter the book genre: ")
    availability_status = True

    # Dictionary
    book = {
        'id': book_id,
        'title': title,
        'author': author,
        'genre': genre,
        'available': availability_status
        }
    
    # Append then add one digit to id to make it 2, 3, and it goes on
    books.append(book)
    # Final output
    print(f"THe book, {title} is added!\nThe book ID: {book_id}")
    book_id = book_id + 1

def view_books():
    # Display books using if and else
    if not books:
        print("\nNo books in the library yet.")
    
    # if and else branches
    print("\nBooks that are available in library")
    for book in books:
        if book['available']:
            status = "Available"
        else:
            status = "Borrowed"

        print(f"\nID: {book['id']}, Title: {book['title']}")
        print(f"Author: {book['author']}, Genre: {book['genre']}, Status: {status}")

def front_page():
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Exit") 
        
        # User's input
        choice = input("Enter your choice: ")
        
        # if, elif, and else branches
        if choice == '1':
            book_management()
        elif choice == '2':
            view_books()
        elif choice == '3':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Call functions
front_page()


