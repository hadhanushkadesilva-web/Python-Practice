def get_number(prompt):
    """Ask for a number repeatedly until user gives a valid one."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️  Not a valid number. Please try again.")

def get_operation():
    """Ask for an operation repeatedly until valid."""
    valid_ops = ["+", "-", "*", "/"]
    while True:
        op = input("Choose operation (+, -, *, /): ")
        if op in valid_ops:
            return op
        print("⚠️  Invalid operation. Please choose +, -, *, or /.")

def calculate(a, b, op):
    """Perform the operation. Raises ZeroDivisionError if dividing by zero."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

# Main loop
print("=== BULLET-PROOF CALCULATOR ===")
while True:
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    op = get_operation()

    try:
        result = calculate(a, b, op)
        print(f"✓ Result: {a} {op} {b} = {result}")
    except ZeroDivisionError as e:
        print(f"⚠️  {e}")

    again = input("\nAnother calculation? (y/n): ")
    if again.lower() != "y":
        print("Goodbye!")
        break