"""
1.Wykorzystaj funkcję input() wbudowaną w python do
    pobrania informacji od użytkownika z konsoli.
    Poproś użytkownika o podanie imienia, nazwiska, miasta
    Zapisz te informacje w zmiannych name, surname i city
2.Wyświetl w konsoli tekst podsumowujący pobrane dane:
    "Nazywasz się Ania Kowalska i mieszkasz w mieście: Krk"
"""

name = input("Enter your name: ")
surname = input("Enter your surname: ")
city = input("Enter your city: ")

print("Nazywasz się " + name + " " + surname + " i mieszkasz w mieście: " + city)