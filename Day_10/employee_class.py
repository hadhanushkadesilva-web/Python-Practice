class Employee:
    def __init__(self, name, employee_id, department, salary, hire_year):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.hire_year = hire_year
    
    def give_raise(self, amount):
        self.salary += amount
        
    def promote(self, new_department):
        self.department = new_department
        
    def years_at_company(self, current_year):
        return current_year - self.hire_year
    
    def is_senior(self):
        return self.years_at_company(2026) >= 5
    
    def __str__(self):
        return f"[{self.employee_id}] {self.name} - {self.department} - ${self.salary:,.2f} "
      
        
        

# Create 3 employees
emp1 = Employee("Anna Silva", 101, "Engineering", 50000, 2020)
emp2 = Employee("Bob Karunaratne", 102, "Marketing", 45000, 2018)
emp3 = Employee("Cathy De Silva", 103, "HR", 40000, 2022)

# Print all three (tests __str__)
print("=== Initial state ===")
print(emp1)
print(emp2)
print(emp3)

# Give Anna a raise
emp1.give_raise(5000)
print(f"\nAfter Anna's raise: {emp1}")

# Promote Bob
emp2.promote("Sales")
print(f"After Bob's promotion: {emp2}")

# Check years at company and seniority
print(f"\n--- Seniority check (current year 2026) ---")
for emp in [emp1, emp2, emp3]:
    years = emp.years_at_company(2026)
    senior = emp.is_senior()
    print(f"{emp.name}: {years} years | senior? {senior}")