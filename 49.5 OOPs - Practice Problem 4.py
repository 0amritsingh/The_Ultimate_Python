# Problem: Define an employee class with attributes role, department and salary. This class also has a showDetails() methods. Create an Engineer class that inherits properites from employee and has additional attributes: name and age

class employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showDetails(self):
        print(f'Role: {self.role}\nDepartment: {self.department}\nSalary: {self.salary}')

class engineer(employee):
    def __init__(self, name, age):
        super().__init__('Engineer', 'IT', 75000)
        self.name = name
        self.age = age

e = employee('SDE 1', 'AI', 250000)
e.showDetails()
print()
e = engineer('Amrit Singh', 18)
e.showDetails()