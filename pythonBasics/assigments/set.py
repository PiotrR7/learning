"""
1. Stwórz set z unikalnymi wartościami jak:
    Ania, Kasia, Ola, Karol, Daniel, Zuza
2. Dodaj do set za pomocą funkcji add kolejne elementy:
    Olek, Basia, Kasia, Karol, Zuza, Paulina
3. Pokaż w konsoli wielkość set
4. Wykorzystaj petlę for aby pokazać elementy w set
"""

data = {"Ania", "Kasia", "Ola", "Karol", "Daniel", "Zuza"}
data.add("Olek")
data.add("Basia")
data.add("Kasia")
data.add("Karol")
data.add("Zuza")
data.add("Paulina")

print(len(data))

for element in data:
    print(element)