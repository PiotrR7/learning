class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.mileage = 1
        self.setTopSpeed(230)
        self.printInfo()

    def printInfo(self):
        print(self.brand, self.model, self.color, self.year, self.mileage, self.topSpeed)

    def setTopSpeed(self, speed):
        self.topSpeed = speed

mustang = Car("Ford", "Mustang", "red", 1970)
mustang.mileage = 100
mustang.setTopSpeed(320)
mustang.printInfo()

charger = Car("Dodge", "Charger", "blue", 1971)