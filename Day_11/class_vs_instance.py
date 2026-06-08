class Employee:
    company = "Acme Inc."         # class attribute — shared
    raise_rate = 0.05              # class attribute — shared default

    def __init__(self, name, salary):
        self.name = name           # instance attribute
        self.salary = salary       # instance attribute

    def give_raise(self):
        # Uses the SHARED class attribute
        self.salary += self.salary * Employee.raise_rate


# Create employees
emp1 = Employee("Anna", 50000)
emp2 = Employee("Bob", 45000)

# Read class attribute via instance
print(f"{emp1.name} works at {emp1.company}")
print(f"{emp2.name} works at {emp2.company}")

# Give them raises (using the shared rate)
emp1.give_raise()
emp2.give_raise()
print(f"\nAfter 5% raise: {emp1.name} = ${emp1.salary}, {emp2.name} = ${emp2.salary}")

# Change the CLASS attribute — both instances see it
Employee.company = "Acme Holdings Ltd."
print(f"\n--- After company rename ---")
print(f"{emp1.name} now works at {emp1.company}")
print(f"{emp2.name} now works at {emp2.company}")

# Now do a SNEAKY mistake — assign via instance
emp1.company = "Anna's Custom Co."
print(f"\n--- After sneaky emp1.company assignment ---")
print(f"emp1.company: {emp1.company}")
print(f"emp2.company: {emp2.company}")
print(f"Employee.company: {Employee.company}")