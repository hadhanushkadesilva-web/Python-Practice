# 1. Lambda assigned to a name (rare, but legal)
square = lambda x: x * x
print(f"square(5) = {square(5)}")

# 2. Lambda with multiple parameters
add = lambda a, b: a + b
print(f"add(3, 7) = {add(3, 7)}")

# 3. Lambda that returns True/False
is_even = lambda n: n % 2 == 0
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")

# 4. Lambda for a simple discount calculation
discount = lambda price, pct: price - (price * pct / 100)
print(f"Discount on $100 at 20% = ${discount(100, 20)}")

# 5. The REAL way lambda shines — inline with sorted()
students = [("Anna", 85), ("Bob", 72), ("Cathy", 95), ("Diana", 68)]

# Sort by NAME (default — alphabetical by first item)
print(f"\nBy name: {sorted(students)}")

# Sort by GRADE (using lambda key)
print(f"By grade ascending:  {sorted(students, key=lambda s: s[1])}")
print(f"By grade descending: {sorted(students, key=lambda s: s[1], reverse=True)}")