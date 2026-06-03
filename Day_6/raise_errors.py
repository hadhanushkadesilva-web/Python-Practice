def withdraw(amount, balance):
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if amount > balance:
        raise ValueError(f"Insufficient funds. Balance: ${balance}, requested: ${amount}.")
    return balance - amount

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age seems unrealistic.")
    return age

# --- Test withdraw() ---
print("--- Withdraw tests ---")

# Test 1: valid withdrawal
try:
    new_balance = withdraw(50, 200)
    print(f"✓ New balance: ${new_balance}")
except ValueError as e:
    print(f"⚠️  {e}")

# Test 2: invalid (negative amount)
try:
    new_balance = withdraw(-10, 200)
    print(f"✓ New balance: ${new_balance}")
except ValueError as e:
    print(f"⚠️  {e}")

# Test 3: invalid (more than balance)
try:
    new_balance = withdraw(500, 100)
    print(f"✓ New balance: ${new_balance}")
except ValueError as e:
    print(f"⚠️  {e}")

# --- Test set_age() ---
print("\n--- Age tests ---")
for test_age in [25, -3, 200]:
    try:
        age = set_age(test_age)
        print(f"✓ Age accepted: {age}")
    except ValueError as e:
        print(f"⚠️  {e}")