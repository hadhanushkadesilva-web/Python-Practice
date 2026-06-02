# Part 1 — a tuple of coordinates
point = (3, 4)
print(f"Point: {point}")
print(f"X = {point[0]}, Y = {point[1]}")
print(f"Length of tuple: {len(point)}")

# Part 2 — try to change a tuple (this will FAIL — that's the point)
# Uncomment the next line to see the error, then comment it back:
# point[0] = 99

# Part 3 — unpacking a tuple
person = ("Dhanushka", 35, "Sri Lanka")
name, age, country = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")

# Part 4 — unpacking inside a for loop (this is COMMON in real code)
people = [
    ("Anna", 25, "USA"),
    ("Bob", 40, "UK"),
    ("Cathy", 30, "Canada"),
]

print("\nPeople list:")
for name, age, country in people:
    print(f"{name} is {age} years old, from {country}.")