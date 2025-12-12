"""
1. Zadeklaruj zmienna 'number' z int o wartości 5 i wyświetl jej adres w pamięci
2. Zwiększ wartośc zmiennej 'number' o 2 i ponownie wyświetl jej adres w pamięci
3. Utwórz listę 'fruits' z trzema owocami: "apple", "banana", "cherry".
    Wyświetl adres w pamięci listy
4. Dodaj do listy 'fruits' kolejny owoc: "orange" i wyświetl adres w pamięci listy.
5. Na podstawie wykonanych czynności wyjaśnij różnicę między typami mutowalnymi, a niemutowalnymi
"""

number = 5
print(id(number))

number += 2
print(id(number))

fruits = ['apple', 'banana', 'cherry']
print(id(fruits))

fruits.append('orange')
print(id(fruits))

# Na podstawie wykonanych czynności wnioskujemy, że zmienna number o typie int po zmianie
# wartości zmienia się również jej miejsce w pamięci co oznacza, że jest niemutowalna.
# Lista fruits w przeciwieństwie do int po zmianie wartości nie zmienia swojego miejsca
# w pamięci, co oznacza że jest mutowalna.