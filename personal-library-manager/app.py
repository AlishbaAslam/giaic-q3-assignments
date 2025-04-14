import json
import os

# File to store book shelf data
my_books = 'library.txt'

# Load library from file if it exists
def load_library():
    if os.path.exists(my_books):
        with open(my_books, 'r') as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(my_books, 'w') as file:
        json.dump(library, file)

# Add a new book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: ").strip())
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!\n")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

# Search books by title or author
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    query = input("Enter the search term: ").strip().lower()

    filtered_books = []
    if choice == "1":
        filtered_books = [b for b in library if query in b["title"].lower()]
    elif choice == "2":
        filtered_books = [b for b in library if query in b["author"].lower()]
    else:
        print("Invalid choice.\n")
        return

    if filtered_books:
        print("Matching Books:")
        for i, book in enumerate(filtered_books, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.\n")
        return

    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Show statistics
def display_statistics(library):
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    percentage = (read_count / total * 100) if total > 0 else 0

    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%\n")

# Menu loop
def main():
    library = load_library()
    while True:
        print()
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit\n")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
