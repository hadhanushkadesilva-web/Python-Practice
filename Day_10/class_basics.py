# Define the Book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Create 3 book instances
book1 = Book("Atomic Habits", "James Clear", 2018)
book2 = Book("Sapiens", "Yuval Noah Harari", 2011)
book3 = Book("Deep Work", "Cal Newport", 2016)

# Access attributes
print(f"Book 1: {book1.title} by {book1.author} ({book1.year})")
print(f"Book 2: {book2.title} by {book2.author} ({book2.year})")
print(f"Book 3: {book3.title} by {book3.author} ({book3.year})")

# Access ONE attribute
print(f"\nThe author of '{book1.title}' is {book1.author}.")

# Type checking
print(f"\nWhat type is book1? {type(book1)}")