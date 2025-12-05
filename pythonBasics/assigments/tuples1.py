"""
1.Stwórz krotkę z wartościami: 50, 100, 150, 200, 250
2.Pokaż typ krotki w konsoli
3.Pokaż w konsoli ilość elementów krotki
4.Pokaż ostatni element krotki wykorzystując len() - 1
5.Następnie pokaż elementy od drugiego do czwartego
6.Pokaż trzeci element od końca z ujemnym indeksem
"""

tuple1 = (50, 100, 150, 200, 250)

print(type(tuple1))
print(len(tuple1))
print(tuple1[len(tuple1)-1])
print(tuple1[1:4])
print(tuple1[-3])