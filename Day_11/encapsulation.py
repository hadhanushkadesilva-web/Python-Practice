class BankAccount:
    def __init__(self, owner, opening_balance):
        self.owner = owner             # public
        self.__balance = opening_balance   # private

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account [{self.owner}] balance: ${self.__balance:,.2f}"
# Test code
acc = BankAccount("Dhanushka", 1000)

# Public attribute — works
print(f"Owner: {acc.owner}")

# Private — must go through method
print(f"Balance via method: ${acc.get_balance()}")

# Deposit and withdraw
acc.deposit(500)
acc.withdraw(200)
print(acc)

# Try invalid operations — should raise errors
try:
    acc.withdraw(99999)       # too much
except ValueError as e:
    print(f"⚠️ {e}")

try:
    acc.deposit(-100)         # negative
except ValueError as e:
    print(f"⚠️ {e}")

# Try to directly access private — should FAIL
try:
    print(acc.__balance)
except AttributeError as e:
    print(f"⚠️ Cannot access private directly: {e}")