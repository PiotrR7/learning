"""
    Typy w Python można podzielić na dwie kategorie mutowalne oraz niemutowalne.
    Mutowalne to takie których wartość można zmienić, natomiast typy niemutowalne
    nie można zmienić.Do rozważań wykorzystamy specjalną funkcję id), która zwraca
    unikalny identyfikator dla każdego przekazanego obiektu, w praktyce jest to liczba
    całkowita określająca miejsce w pamięci, gdzie przechowywana jest wartość.
    Pamiętajmy że w Python wszystko jest obiektem np liczby całkowite, float, krotki itd.
"""

# typy: int, float, bool, str, tuple, frozenset są niemutowalne
# typy: list, set, dict są mutowalne

a = 1
addr1 = id(a)

a += 1
addr2 = id(a)

print(addr1, "\n", addr2, "\n", addr1 == addr2)


listData = [1, 2, 3]
addr1 = id(listData)

listData.append(4)
addr2 = id(listData)

print(addr1, "\n", addr2, "\n", addr1 == addr2)