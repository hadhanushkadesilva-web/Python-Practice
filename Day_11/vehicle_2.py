class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        return f"{self.brand} ({self.year})"
    
class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)  # Call the parent constructor
        self.num_doors = num_doors

    def describe(self):
        return f"{self.brand} ({self.year}) - {self.num_doors} doors"

v = Vehicle("Honda", 2018)
c = Car("Toyota", 2020, 4)
print(v.describe())     # Honda (2018)
print(c.describe())     # Toyota (2020) — 4 doors
print(isinstance(c, Vehicle))   # True       