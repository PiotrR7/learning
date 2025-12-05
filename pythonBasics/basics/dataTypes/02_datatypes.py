#Python jest językiem z typami dynamicznymi, tzn. do tej samej zmiennej możemy przypisać różne wartości

#Typy liczbowe
"""
int - liczba całkowita
float - liczba zmiennoprzecinkowa, rzeczywista
complex - liczba zespolona będąca sumą części rzeczywistej oraz urojonej (oznaczoną literą j)
"""

numInt = 5
numFloat = 3.14
numComplex = 5 + 3j

print(type(numInt))
print(type(numFloat))
print(type(numComplex))

#Łańcuchy znaków - String
text = "Hello World!"
print(text)
print(len(text))
print(type(text))

multiLine = """
    pierwsza linia
    druga linia
    trzecia linia
"""
print(multiLine)

multiLine2 = "pierwsza linia\n\tdruga linia\ntrzecia linia"
print(multiLine2)

#Wartość logiczna - Boolean
t = True
f = False

print(type(t))

#Typ list - list
list1 = [1, 2, 3]
print(type(list1))
print(len(list1))

del list1[0]
isInList = 2 in list1

list2 = [
    [1, 2, 3],
    [4, 5, 6],
]

#Typ krotki - Tuples
"""
    Krotki są niemutownalne, czyli nie można zmieniać jej wartości,
    próba jej przypisania spowoduje błąd.
"""

data = ("Ala", "Ola", "Kasia")
# data[0] = "Rafał" - błąd

name = data + ("Rafał",)
print(type(name))

#Typ Dict - słownik
"""
    Słownik to zbiór par kluczy oraz wartości, klucze muszą być unikalne
    i służą do pobrania wartości. Elementy w słowniku nie mają kolejności, nie jest to lista.
"""

contacts = {
    "Ola" : "ola@example.com",
    "Daniel" : 30,
    "Ania" : "ania@example.com"
}

contacts["Rafał"] = "rafal@example.com"
print(contacts["Ola"])
print(type(contacts))
print(contacts.keys())
print(contacts.values())

#Typ Set i Frozenset - zbiór
"""
    set - zestaw to nieuporządkowany zbiór unikalnych wartości
    Zestaw nie pozwala na dodanie zduplikowanych elementów,
    jest iterowalny, zmienny, nie posiada pozycji elementów - indeksu.
    Jego odmianą jest frozenset, który jest niezmienny / niemutowalny.
    Zestaw zapisywany jest za pomocą nawiasów klamrowych i wartości po przecinku.
"""

setData = {2, 3, 1, 4, 5}
setData.add(22)
setData.discard(1)
print(type(setData))

frozenData = frozenset(setData)
print(type(frozenData))

#Typ None
currentTaskNumber = 10
currentTaskNumber = None
currentTaskNumber = 2