nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Double every number with map
doubled = list(map(lambda x: x * 2, nums))
print(f"Doubled: {doubled}")

# 2. Keep only multiples of 3 with filter
multiples_of_3 = list(filter(lambda x: x % 3 == 0, nums))
print(f"Multiples of 3: {multiples_of_3}")

# 3. Combine — squares of even numbers
even_squares = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))
print(f"Squares of evens: {even_squares}")

# 4. Same thing — comprehension version (compare!)
even_squares_2 = [x * x for x in nums if x % 2 == 0]
print(f"Same with comprehension: {even_squares_2}")

# 5. Real-world example — filter Python files from a list of filenames
files = ["main.py", "data.csv", "test.py", "config.json", "app.py", "readme.md"]
python_files = list(filter(lambda f: f.endswith(".py"), files))
print(f"\nPython files: {python_files}")

# 6. Real-world example — convert all temperatures using map
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(f"Fahrenheit: {fahrenheit}")