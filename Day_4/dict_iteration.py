prices = {
    "Bread": 2.50,
    "Milk": 3.00,
    "Eggs": 4.50,
    "Apples": 5.25,
    "Tea": 2.00
}

# Way 1 — print all item names (keys)
print("Items we sell:")
for item in prices.keys():
    print(item)

# Way 2 — print all prices (values)
print("\nAll prices:")
for price in prices.values():
    print(f"${price:.2f}")

# Way 3 — print each item with its price (the BEST way)
print("\nFull menu:")
for item, price in prices.items():
    print(f"{item}: ${price:.2f}")

# Way 4 — calculate the total of all values
print("\nTotal value of stock:")
total = 0
for price in prices.values():
    total = total + price
print(f"Sum: ${total:.2f}")