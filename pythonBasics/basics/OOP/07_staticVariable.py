class Employee:
    "Employee class describing company employee"
    numEployees = 0
    emplyeesList = []

    def __init__(self, name):
        "Constructor for Employee"
        self.name = name
        Employee.numEployees += 1
        Employee.emplyeesList.append(self)

        print(self.name, "Liczba pracowników: ", Employee.numEployees)

    def printAllEmployees(self):
        for el in Employee.emplyeesList:
            print(el.name)

employee = Employee("Ola")
employee1 = Employee("Asia")
employee2 = Employee("Kasia")

print(employee.numEployees)
employee.printAllEmployees()

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)

print("name attr in Employee: ", hasattr(Employee, "name"))
print("city attr in Employee: ", hasattr(Employee, "city"))

print("employee1.name: ", getattr(employee1, "name"))

setattr(employee1, "name", "Michael")
print("employee1.name: ", employee1.name)
