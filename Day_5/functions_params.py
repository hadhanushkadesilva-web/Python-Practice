# Function 1 — one parameter, no return
def greet(name):
    print(f"Hello, {name}!")

# Function 2 — two parameters, with return
def add(a, b):
    return a + b

# Function 3 — calculate area of a rectangle
def area_of_rectangle(width, height):
    return width * height

# Function 4 — check if a number is even (returns True/False)
def is_even(number):
    return number % 2 == 0

# --- Use them ---
greet("Dhanushka")
greet("Anna")

# Use the return values
total = add(10, 20)
print(f"10 + 20 = {total}")

big_total = add(total, 5)             # using add's return AS an argument!
print(f"Adding 5 more: {big_total}")

area = area_of_rectangle(4, 6)
print(f"Area = {area}")

print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")