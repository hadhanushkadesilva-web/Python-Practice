# Function 1 — greet with optional greeting
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Function 2 — calculate price after discount
def apply_discount(price, discount=10):
    discounted_price = price - (price * discount / 100)
    return discounted_price

# Function 3 — print a separator (default char and width)
def print_separator(char="-", width=20):
    print(char * width)

# --- Call them ---
greet("Anna")                          # uses default greeting
greet("Bob", "Hi")                     # custom greeting
greet("Cathy", greeting="Howdy")       # keyword argument

print_separator()                      # default - and 20
print_separator("=", 30)               # custom = and 30
print_separator(width=10)              # only override width

print(f"Price after default 10% discount: ${apply_discount(100):.2f}")
print(f"Price after 25% discount: ${apply_discount(100, 25):.2f}")
print(f"Price after 50% discount: ${apply_discount(price=200, discount=50):.2f}")