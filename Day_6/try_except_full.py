# Safe divider with full structure
def safe_divide():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ValueError:
        print("⚠️  Please enter whole numbers only.")
    except ZeroDivisionError:
        print("⚠️  Cannot divide by zero.")
    else:
        print(f"✓ Result: {result}")
    finally:
        print("(Division attempt finished.)")

# Run it 3 times to test each path
print("--- Run 1 ---")
safe_divide()

print("\n--- Run 2 ---")
safe_divide()

print("\n--- Run 3 ---")
safe_divide()