import random

class Student:
    def __init__(self, firstName, lastName, age, city):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfstudy = None

    def printInfo(self):
        print(self.firstName, self.lastName, self.age, self.city, self.schoolName, self.fieldOfstudy)

class School:
    def __init__(self, schoolName, city):
        self.schoolName = schoolName
        self.city = city
        self.studentsList = []
        self.fieldsOfstudy = ["IT", "Math", "Robotics"]

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentsList.append(student)
            student.schoolName = self.schoolName
            student.fieldsOfstudy = random.choice(self.fieldsOfstudy)

    def printInfo(self):
        print(f"Nazwa: {self.schoolName}\nMiejscowość: {self.city}\nLista studentów:")
        for student in self.studentsList:
            print(f"{student.firstName} {student.lastName},")


student1 = Student("Jan", "Kowalsky", 20, "Warsaw")
student1.printInfo()

school = School("Tech School", "Warsaw")
school.addStudent(student1)

student1.printInfo()
school.printInfo()