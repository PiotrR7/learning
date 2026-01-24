from products import *

class Cart:
    def __init__(self):
        self.__productsList = []
        self.__cartValue = 0

    def addProduct(self, product):
        if isinstance(product, Product):
            self.__productsList.append(product)
            self.calculateCart()

    def calculateCart(self):
        self.__cartValue = 0
        for product in self.__productsList:
            self.__cartValue += product.price

    def __str__(self):
        strData = "\nCart: "
        for product in self.__productsList:
            strData += str(product.name) + ": " + str(product.price) + "\n"
        strData += "\nCart value: " + str(self.__cartValue)
        return strData