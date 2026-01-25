import os
import pickle

scriptDir = os.path.dirname(__file__)

class Person:
    def __init__(self, firstName, lastName, city):
        self.firstName = firstName
        self.lastName = lastName
        self.city = city

    def __str__(self):
        return f'{self.firstName} {self.lastName} {self.city}'

person1 = Person('John', 'Doe', city = 'New York')
person2 = Person('Jan', 'Kowalsky', 'Warsaw')

people = [person1, person2]

fh = open(scriptDir + '/people.dat', 'wb')
pickle.dump(people, fh)
fh.close()

fh = open(scriptDir + '/people.dat', 'rb')
listFromFile = pickle.load(fh)
fh.close()

for person in listFromFile:
    print(person)