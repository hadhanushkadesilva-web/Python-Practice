# 1. Cubes of 1 through 5
cubes = [n ** 3 for n in range(1, 6)]
print(f"Cubes: {cubes}")

# 2. Squares of even numbers from 1 to 10
even_squares = [n * n for n in range(1, 11) if n % 2 == 0]
print(f"Even squares: {even_squares}")

# 3. Uppercase first letter of each word
words = ["python", "fastapi", "docker", "git"]
caps = [w.capitalize() for w in words]
print(f"Capitalized: {caps}")

# 4. Filter — keep only words longer than 4 characters
long_words = [w for w in words if len(w) > 4]
print(f"Long words: {long_words}")

# 5. Convert a list of temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(f"Fahrenheit: {fahrenheit}")

# 6. Get the LENGTH of each item in a list
items = ["pen", "notebook", "pc", "headphones"]
lengths = [len(item) for item in items]
print(f"Lengths: {lengths}")