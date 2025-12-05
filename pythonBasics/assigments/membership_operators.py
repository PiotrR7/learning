"""
1. Sprawdź, czy liczba 7 znajduje się w liście 'numbers' i wyświetl odpowiedni komunikat
2. Sprawdź, czy ciąg znaków "kot" nie znajduje się w tuple 'animals' i wyświetl odpowiedni komunikat
3. Stwórz słownik 'user' z kluczami 'name' i 'age'. Sprawdź, czy klucz 'name' znajduje się w słowniku.
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(7 in numbers)

animals = ('dog', 'cat', 'rabbit')
print("kot" in animals)

user = {
    "name": "age",
}
print("name" in user.keys())