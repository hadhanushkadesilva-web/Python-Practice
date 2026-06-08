class Employee:
    company = "Acme Inc."        # class attribute

    def __init__(self, name, salary, hire_year):
        self.name = name
        self.salary = salary
        self.hire_year = hire_year

    def years_at_company(self, current_year=2026):
        return current_year - self.hire_year

    def __str__(self):
        return f"{self.name} - ${self.salary:,.2f}"
    
class Manager(Employee):
    def __init__(self, name, salary, hire_year,team_size=0, bonus_rate=0.1):
        super().__init__(name, salary, hire_year)  # call parent constructor
        self._reports = []  # private attribute to hold direct reports
        self.team_size = team_size
        self.bonus_rate = bonus_rate

    def add_report(self, employee):
        self._reports.append(employee)

    def calculate_bonus(self): 
        return self.salary * self.bonus_rate
    
    def approve_raise(self, employee, percent):
        if employee in self._reports:
            amount = employee.salary * percent / 100
            employee.salary += amount
            print(f"Approved raise of ${amount:,.2f} for {employee.name}. New salary: ${employee.salary:,.2f}")
        else:
            print(f"{employee.name} is not a direct report. Cannot approve raise.")
    def __str__(self):
        return f"{self.name} [Manager] - ${self.salary:,.2f} Team of {self.team_size}"

mgr = Manager("Sarah", 90000, 2018, team_size=5)
emp1 = Employee("Anna", 50000, 2020)
emp2 = Employee("Bob", 45000, 2019)   

mgr.add_report(emp1)
mgr.add_report(emp2)

print(mgr)
print(emp1)
print(emp2)

print(f"\nSarah's bonus: ${mgr.calculate_bonus():,.2f}")

mgr.approve_raise(emp1, 10)
print(f"After raise: {emp1}")

print(f"\nIs Sarah a Manager? {isinstance(mgr, Manager)}")
print(f"Is Sarah an Employee? {isinstance(mgr, Employee)}")
print(f"Sarah's years at company: {mgr.years_at_company(2026)}")