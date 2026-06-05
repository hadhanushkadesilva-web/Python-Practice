class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_recent(self):
        return self.year >= 2015

    def reprint(self, new_year):
        self.year = new_year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"


book1 = Book("Atomic Habits", "James Clear", 2018)
book2 = Book("Sapiens", "Yuval Noah Harari", 2011)
book3 = Book("Deep Work", "Cal Newport", 2016)

# Try printing directly
print(book1)
print(book2)
print(book3)

# In f-strings
print(f"\nMy top pick is: {book1}")

# In a list — interesting!
books = [book1, book2, book3]
print(f"\nAll books: {books}")    # ← what happens here? Predict!