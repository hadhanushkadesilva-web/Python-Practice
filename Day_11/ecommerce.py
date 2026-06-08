class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.stock = stock

    def get_price(self):
        return self.__price

    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount must be between 0 and 100.")
        self.__price = self.__price * (1 - percentage / 100)
      
    def is_in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return f"{self.name} ( ${self.__price:.2f} , stock: {self.stock} )"
    
class PhysicalProduct(Product):
    def __init__(self, name, price, stock, weight_kg):
        super().__init__(name, price, stock)
        self.weight = weight_kg

    def __str__(self):
        return f"{super().__str__()} , {self.weight} kg"

class DigitalProduct(Product):
    def __init__(self, name, price, stock, download_url):
        super().__init__(name, price, stock)
        self.download_url = download_url

    def __str__(self):
        return f"{super().__str__()} , Download : {self.download_url}"
    
# Test code
apple = PhysicalProduct("Apple", 1.50, 20, 0.2)
ebook = DigitalProduct("Python Book", 9.99, 99, "https://example.com/dl/123")

print(apple)
print(ebook)

print(f"\nApple price: ${apple.get_price()}")
print(f"In stock? {apple.is_in_stock()}")

# Apply discounts
apple.apply_discount(10)
ebook.apply_discount(20)
print(f"\nAfter discounts:")
print(apple)
print(ebook)

# Try invalid discount
try:
    ebook.apply_discount(150)
except ValueError as e:
    print(f"⚠️ {e}")

# Try direct access to private price
try:
    print(apple.__price)
except AttributeError as e:
    print(f"⚠️ Can't access private: {e}")

# Confirm inheritance
print(f"\nIs apple a Product? {isinstance(apple, Product)}")
print(f"Is ebook a Product? {isinstance(ebook, Product)}")
print(f"Is apple a DigitalProduct? {isinstance(apple, DigitalProduct)}")