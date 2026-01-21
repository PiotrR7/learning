class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor!")

    def printPersonData(self):
        print("Person.printPersonData:", self.name, self.surname, self.city)

person1 = Person("Jan", "Kowalsky", "Krk")
person1.printPersonData()

class Employee(Person):
    def __init__(self, name, surname, city, companyName, salary):
        Person.__init__(self, name, surname, city)

        self.companyName = companyName
        self.salary = salary
        print("Employee constructor!")

    def printEmployeeData(self):
        print("Employee.printEmployeeData:", self.companyName, self.salary)

employee1 = Employee("Jan", "Kowalsky", "Waw", "tech-land", 100000)
employee1.printPersonData()
employee1.printEmployeeData()

class Manager(Employee):
    def __init__(self, name, surname, city, companyName, salary, department):
        Employee.__init__(self, name, surname, city, companyName, salary)
        self.department = department

    def hireEmployee(self):
        print("Hire employee!")

    def printManagerData(self):
        print("Manager.printManagerData:", self.department)

manager1 = Manager("Jan", "Kowalsky", "Waw", "tech-land", 1000, "IT")
manager1.printPersonData()
manager1.printEmployeeData()
manager1.printManagerData()
manager1.hireEmployee()