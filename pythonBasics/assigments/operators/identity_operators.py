"""
1. Stwórz zmienną 'text' z wartością "Hello" i użyj metody upper()
    do wyświetlenia wielkich liter. Sprawdź dostępne metody za pomocą dir()
2. Stwórz dwie zmienne 'x' i 'y' i wartością 256. Sprawdź czy x is y.
3. Stwórz listę 'listOne' z kilkoma elementami. Skopiuj 'listOne' do 'listTwo'
    poprzez przypisanie. Sprawdź, czy listOne is listTwo
4. Zmodyfikuj 'listOne' przez dodanie nowego elementu. Sprawdź, czy zmiana
    wpłynęła na 'listTwo'. Użyj if do wyświetlania komunikatu o zmianie.
5. Stwórz nową listę 'listThree' z takimi samymi elementami, co'listOne'.
    Sprawdź, czy listOne is listThree i wyświetl odpowiedni komunikat za pomocą if.
"""

text = "Hello"
print(text.upper())
print(dir(text))

x,y = 256, 256
print(x is y)

listOne = [1, 2, 3]
listTwo = listOne
print(listOne is listTwo)

listOne.append(4)
if listOne is listTwo:
    print("Zmiana wpłynęła na listTwo")

listThree = [1, 2, 3, 4]
if listThree is listOne:
    print("listThree is listOne")
else:
    print("listThree is not listOne")