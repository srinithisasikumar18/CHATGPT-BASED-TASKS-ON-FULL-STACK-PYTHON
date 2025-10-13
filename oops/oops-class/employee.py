class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def display_details(self):
        print(f"Name:{self.name} Salary:{self.salary} Department:{self.department}")
    def give_raise(self,amount):
        self.salary+=amount
e1=Manager("srinithi",75000.00,"IT")
e1.give_raise(10000.30)
e1.display_details()