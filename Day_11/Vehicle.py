from turtle import speed


class Vehicle:
    fuel_type = "Petrol"  # Class attribute shared by all vehicles
    
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def describe(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h., Fuel Type: {self.fuel_type}"

class ElectricVehicle(Vehicle):
    
    fuel_type = "Electric"  # Override the fuel type for electric vehicles
    
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed)  # Call parent constructor
        self.battery_capacity = battery_capacity
    
    def describe(self):
        base_description = super().describe()
        return f"{base_description} Battery Capacity: {self.battery_capacity} kWh."

# Create instances
car1 = Vehicle("Toyota", 180)
ev1 = ElectricVehicle("Tesla", 250, 100)

print(car1.describe())
print(ev1.describe())
    