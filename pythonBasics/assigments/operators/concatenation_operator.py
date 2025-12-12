"""
1. Połącz 2 stringi 'firstName' i 'lastName' w jeden string 'fullName'
    i wyświetl go. Dodaj między nimi spację.
2. Stwórz 2 listy: 'listOne' z liczbami 1-3 i 'listTwo' z liczbami 4-6.
    Połącz je w jedną listę 'combinedList' i wyświetl.
3. Jeśli długość combinedList jest większa od 5, wyświetl "Lista jest długa".
4. Do zmiennej 'greeting' dodaj string 'Hello', a do niej 'fullName'.
    Sprawdź, czy w 'greeting' znajduje się słowo 'Hello'. Jeśli tak,
    wyświetl pełne powitanie.
"""

firstName = "John"
lastName = "Kowalsky"
fullName = firstName + " " + lastName

listOne = [1, 2, 3]
listTwo = [4, 5, 6]
combinedList = listOne + listTwo

if len(combinedList) > 5:
    print("Lista jest długa")

greeting = "Hello " + fullName
if "Hello" in greeting:
    print(greeting)