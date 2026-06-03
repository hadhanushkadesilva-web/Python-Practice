# Test 1 — runs OK
print("Test 1 — valid input")
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That was not a valid number.")

# Test 2 — divide by zero
print("\nTest 2 — divide by zero")
try:
    a = 10
    b = 0
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Test 3 — dictionary key error
print("\nTest 3 — missing dictionary key")
person = {"name": "Anna", "age": 25}
try:
    print(person["email"])
except KeyError:
    print("That key does not exist in the dictionary.")