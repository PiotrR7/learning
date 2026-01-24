from cart import *

phone = Phone("Phonx", 1000, "black")
tv = TV("TVy", 3000, 60)

cart = Cart()
cart.addProduct(phone)
cart.addProduct(tv)

print(cart)
