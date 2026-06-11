import os
import json

#Producr Class
class Product:
    def __init__(self, name, price, stock, SKU):
        self.name = name
        self.__price = price        # private, encapsulation
        self.stock = stock
        self.SKU = SKU

    def get_price(self):
        return self.__price

    def update_stock(self, amount):
        self.stock += amount        # amount can be negative (sold) or positive (restock)

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.__price,
            "stock": self.stock,
            "SKU": self.SKU
        }

    def __str__(self):
        return f"{self.name} (${self.__price:.2f}, stock: {self.stock}, SKU: {self.SKU})"



# Inventory class
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"✓ Added: {product.name}")

    def remove_product(self, sku):
        for product in self.products:
            if product.SKU == sku:
                self.products.remove(product)
                print(f"✓ Removed {sku}")
                return
        print(f"⚠️ SKU {sku} not found")

    def update_stock(self, sku, amount):
        for product in self.products:
            if product.SKU == sku:
                product.update_stock(amount)
                print(f"✓ Updated stock for {sku}")
                return
        print(f"⚠️ SKU {sku} not found")

    def find_by_name(self, name_query):
        return [p for p in self.products if name_query.lower() in p.name.lower()]

    def show_all(self):
        if not self.products:
            print("Inventory is empty")
            return
        for i, p in enumerate(self.products, start=1):
            print(f"{i}. {p}")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump([p.to_dict() for p in self.products], file, indent=4)
        print(f"✓ Saved {len(self.products)} products to {filename}")

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            print(f"(No existing file '{filename}' — starting empty.)")
            return
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print(f"(File '{filename}' is empty or corrupt — starting empty.)")
            return
        for d in data:
            product = Product(d["name"], d["price"], d["stock"], d["SKU"])
            self.products.append(product)
        print(f"✓ Loaded {len(self.products)} products from {filename}")


# Test code
FILENAME = "products.json"

inv = Inventory()
inv.load_from_file(FILENAME)

inv.add_product(Product("Bread", 2.50, 10, "P001"))
inv.add_product(Product("Milk",  3.00,  5, "P002"))
inv.add_product(Product("Eggs",  4.50, 20, "P003"))

print("\n--- All products ---")
inv.show_all()

print("\n--- Sell 3 breads ---")
inv.update_stock("P001", -3)

print("\n--- Search 'mi' ---")
matches = inv.find_by_name("mi")
for m in matches:
    print(m)

print("\n--- Remove P002 ---")
inv.remove_product("P002")

print("\n--- After removal ---")
inv.show_all()

print("\n" + "=" * 50)
print("Save to disk")
print("=" * 50)
inv.save_to_file(FILENAME)

print("\n" + "=" * 50)
print("Simulate program restart — fresh Inventory, load from file")
print("=" * 50)
inv2 = Inventory()
inv2.load_from_file(FILENAME)

print("\n--- Loaded from file ---")
inv2.show_all()