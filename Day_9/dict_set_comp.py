# 1. Dict comprehension — map number to its square
squares_dict = {n: n * n for n in range(1, 6)}
print(f"Squares: {squares_dict}")

# 2. Dict comprehension — map student name to grade (string to int)
names = ["Anna", "Bob", "Cathy"]
grades = [85, 72, 95]
# Use zip() to pair them up (zip pairs items from two lists)
student_grades = {name: grade for name, grade in zip(names, grades)}
print(f"Student grades: {student_grades}")

# 3. Dict comprehension — filter only passing grades (>= 70)
passing = {name: grade for name, grade in student_grades.items() if grade >= 70}
print(f"Passing: {passing}")

# 4. Set comprehension — unique letters in a phrase
phrase = "comprehension"
unique = {letter for letter in phrase}
print(f"Unique letters in 'comprehension': {unique}")
print(f"How many unique: {len(unique)}")

# 5. Set comprehension — squares modulo 10 (drop duplicates)
mod_squares = {n * n % 10 for n in range(1, 20)}
print(f"Last digits of squares (1-19): {mod_squares}")