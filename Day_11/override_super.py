class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes some sound.")


class Dog(Animal):
    # OVERRIDE — change speak() completely
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    # EXTEND — keep parent behavior AND add to it
    def speak(self):
        super().speak()              # call parent's speak() first
        print(f"... then {self.name} also says Meow!")


class Puppy(Dog):
    # A puppy IS a Dog, but also has age
    def __init__(self, name, age):
        super().__init__(name)       # let Dog (which inherited Animal's __init__) set name
        self.age = age               # add new attribute

    def introduce(self):
        print(f"I'm {self.name}, a puppy aged {self.age} months.")


# --- Test ---
print("--- Test 1: Override ---")
rex = Dog("Rex")
rex.speak()

print("\n--- Test 2: Extend with super() ---")
whiskers = Cat("Whiskers")
whiskers.speak()

print("\n--- Test 3: Multi-level inheritance + super() in __init__ ---")
buddy = Puppy("Buddy", 3)
buddy.introduce()
buddy.speak()                 # inherits Dog's speak (which overrides Animal's)

print(f"\nIs buddy a Puppy? {isinstance(buddy, Puppy)}")
print(f"Is buddy a Dog? {isinstance(buddy, Dog)}")
print(f"Is buddy an Animal? {isinstance(buddy, Animal)}")