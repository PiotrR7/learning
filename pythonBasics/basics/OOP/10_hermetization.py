class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__gears = 5

    def __getGearsInfoStr(self):
        return f"Gears num: {self.__gears}"

    def printInfo(self):
        print(self.brand, self.model, self.__getGearsInfoStr())

vehicle1 = Vehicle("Dodge", "Charger")
vehicle1.printInfo()

print(vehicle1._Vehicle__gears)
print(vehicle1._Vehicle__getGearsInfoStr())

"""
    print(vehicle1.__gears) -error
    print(vehicle1.__getGearsInfoStr()) -error
"""

class Car(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand, model)

car1 = Car("Ford", "Mustang")