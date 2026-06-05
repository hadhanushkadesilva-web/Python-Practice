class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        """Return a one-line description."""
        return f"'{self.title}' by {self.author} ({self.year})"

    def is_recent(self):
        """Return True if the book was published in 2015 or later."""
        return self.year >= 2015

    def reprint(self, new_year):
        """Update the year to a new reprint year."""
        self.year = new_year

# Create 3 books
book1 = Book("Atomic Habits", "James Clear", 2018)
book2 = Book("Sapiens", "Yuval Noah Harari", 2011)
book3 = Book("Deep Work", "Cal Newport", 2016)

# Use the methods
for b in [book1, book2, book3]:
    print(b.describe())
    print(f"  Recent? {b.is_recent()}")

# Modify book2's year via the reprint method
print(f"\nBefore reprint: {book2.describe()}")
book2.reprint(2024)
print(f"After reprint:  {book2.describe()}")
print(f"Recent now?    {book2.is_recent()}")