import json

# Function to load books from the file at the start
def load_books():
    global books
    try:
        with open("library.txt", "r") as file:
            books = [json.loads(line.strip()) for line in file.readlines()]
    except (FileNotFoundError, json.JSONDecodeError):
        books = []  # If file is empty or doesn't exist, start with an empty list

# Function to add a book
def add_book():
    print("\n--- Add a Book ---")
    load_books()
    
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    publication_year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read the book? (yes/no): ").strip().lower() == "yes"

    book = {
        "Title": title,
        "Author": author,
        "Publication Year": publication_year,
        "Genre": genre,
        "Read Status": read_status
    }

    books.append(book)
    
    with open("library.txt", "a") as file:
        file.write(json.dumps(book) + "\n")

    print("Book added successfully!\n")

# Function to remove a book
def remove_book():
    print("\n--- Remove a Book ---")
    load_books()  # Load the latest books before modifying

    title = input("Enter the title of the book to remove: ").strip().lower()
    updated_books = [book for book in books if book["Title"].lower() != title]

    if len(updated_books) == len(books):
        print("No matching book found.\n")
        return

    books[:] = updated_books  # Update the in-memory list

    with open("library.txt", "w") as file:
        for book in books:
            file.write(json.dumps(book) + "\n")

    print(f'"{title}" has been removed successfully!\n')

# Function to search for a book
def search_book():
    print("\n--- Search for a Book ---")
    load_books()  # Searching from the latest file data

    try:
        search_choice = int(input("""Search by:  
        1. Title  
        2. Author  
        Enter your choice: """))
        found = False

        if search_choice == 1:
            search_title = input("Enter the title: ").strip().lower()
            for i, book in enumerate(books):
                if book["Title"].lower() == search_title:
                    print(f"{i+1}. {book['Title']} by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Not Read'}")
                    found = True

        elif search_choice == 2:
            search_author = input("Enter the author: ").strip().lower()
            for i, book in enumerate(books):
                if book["Author"].lower() == search_author:
                    print(f"{i+1}. {book['Title']} by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Not Read'}")
                    found = True

        else:
            print("Invalid choice! Please enter 1 or 2.\n")

        if not found:
            print("No matching books found.\n")
    except ValueError:
        print("Invalid input! Please enter 1 or 2.\n")

# Function to display all books
def display_all_books():
    print("\n--- Display All Books ---")
    load_books()  # Load the latest book list

    if not books:
        print("Your library is empty.\n")
    else:
        for i, book in enumerate(books):
            print(f"{i+1}. {book['Title']} by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Not Read'}")
    print("\n")

# Function to display statistics
def display_statistics():
    print("\n--- Display Statistics ---")
    load_books()  # Load latest data before computing statistics

    total_books = len(books)
    print(f"Total books: {total_books}")

    if total_books > 0:
        read_books = sum(1 for book in books if book["Read Status"])
        print(f"Books Read: {read_books}")
        print(f"Percentage Read: {(read_books/total_books)*100:.2f}%\n")
    else:
        print("No books in your library.\n")

# Main loop
while True:
    try:
        print("""\nWelcome to Your Personal Library Manager!
        1. Add a book  
        2. Remove a book  
        3. Search for a book  
        4. Display all books  
        5. Display statistics  
        6. Exit  """)
        choice = int(input("Enter your choice:  "))

        if choice == 1:
            add_book()
        elif choice == 2:
            remove_book()
        elif choice == 3:
            search_book()
        elif choice == 4:
            display_all_books()
        elif choice == 5:
            display_statistics()
        elif choice == 6:
            print("Exiting... Goodbye!\n")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.\n")
