# Parent class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}!")

    def info(self):
        return f"{self.name} (an animal that says {self.sound})"


# Child class
class Dog(Animal):
    def fetch(self):
        print(f"🐾 {self.name} fetches the ball!")


# Another child class
class Cat(Animal):
    def purr(self):
        print(f"😻 {self.name} purrs softly...")


# Create instances
rex = Dog("Rex", "Woof")
whiskers = Cat("Whiskers", "Meow")

# Test inherited methods
rex.speak()           # from Animal
whiskers.speak()      # from Animal

# Test child-specific methods
rex.fetch()           # Dog only
whiskers.purr()       # Cat only

# Try the inherited info() method
print(rex.info())
print(whiskers.info())

# Type check
print(f"\nIs rex a Dog? {isinstance(rex, Dog)}")
print(f"Is rex an Animal? {isinstance(rex, Animal)}")
print(f"Is whiskers a Dog? {isinstance(whiskers, Dog)}")