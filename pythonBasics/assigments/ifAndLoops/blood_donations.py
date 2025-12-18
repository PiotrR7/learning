"""
1. Dodaj zmienną age o wartości 18 oraz weight = 50
2. Napisz instrukcję if else sprawdzającą, czy kandydat
    ma wiek większy lub równy 18, jeśli tak sprawdź kolejną
    instrukcją if else czy jego waga jest większa lub równa 50.
    Jeśli oba warunki są spełnione napisz w konsoli, że może
    oddać krew.
3. W przypadku gdy jakiś warunek nie jest spełniony, to po else
    napisz w konoli dlaczego
"""

age = 18
weight = 50

if age >= 18:
    if weight >= 50:
        print("Można oddać krew")
    else:
        print("Zbyt mała waga")
else:
    print("Kryterium wieku nie zostało spełnione")