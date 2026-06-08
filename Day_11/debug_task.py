class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        return f"{self.brand} ({self.year})"


class Bike(Vehicle):
    def __init__(self, brand, year, wheels):
        super().__init__(brand, year)  # Call the parent constructor
        self.wheels = wheels

    def describe(self):
        return f"{self.brand} ({self.year}) — {self.wheels} wheels"


# Test code
bike = Bike("Yamaha", 2022, 2)
print(bike.describe())