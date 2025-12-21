"""
1. Wyświetl w konsoli następujące informacje z użyciem pętli w liście
    oraz instrukcji if elif else w celu sprawdzenia, czy liczba jest parzysta,
    czy nie parzysta, oczywiście dodaj informację w konoli
2. Pamiętaj, że 0 będzie oddzielnym przypadkiem, który musisz sprawdzić jako
    pierwszy if i w jej bloku napisz w konsoli tekst: "Zero jest parzyste."
    Następnie w elif sprawdź, czy liczba jest parzysta a oczywiście w else
    będzie pewność, że jest nieparzysta.
"""

data = [-4, -3, -2, -1, 0, 1, 2, 3]

for el in data:
    if el == 0:
        print("Zero jest parzyste.")
    elif el % 2 == 0:
        print("Liczba ", el," jest parzysta.")
    else:
        print("Liczba ", el," nie jest parzysta.")