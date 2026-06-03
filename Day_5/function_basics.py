# Function 1 — say hello (no parameters)
def greet():
    print("Hello, friend!")
    print("Hope you're doing well today.")

# Function 2 — print a line of dashes
def print_line():
    print("-" * 30)

# Function 3 — show today's intro
def show_intro():
    print_line()                       # call another function from inside!
    print("Welcome to Day 5 of Python")
    print_line()

# Now — actually CALL them
greet()
print_line()
show_intro()
greet()