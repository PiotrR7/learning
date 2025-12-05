"""
1. Stwórz zmienną do decimalNum z wartością dziesiętną 45.6789
2. Skonwertuj decimalNum do typu całkowitego (int) i zapisz wynik
    w zmiennej wholeNum. Wyświetl typ zmiennej wholeNum oraz jej wartość.
3. Przekształc łańcuch znaków " 4321 " do typu całkowitego i wyświetl typ po konwersji
4. Stwórz zmienną wholeNum2 z wartością całkowitą 123, następnie skonwertuj
    ją do typu zmiennoprzecinkowego (float) i wyświetl typ oraz wartość
5. Skonwertuj łańcuch znaków "98.76" do typu zmiennoprzecinkowego i wyświetl typ oraz wartość
6. Skorzystaj z funkcji print do wyświetlenia ciągu tekstu zawierającego
    wartość wholeNum2, łącząc ją z tekstem oraz innymi typami danych (np.
    wartością zmiennoprzecinkową, listą). Użyj dwóch metod: konkatenacji za pomocą
    funkcji str() oraz oddzielania wartości przecinkami w funkcji print.
"""

decimalNum = 45.6789
wholeNum = int(decimalNum)
print(type(wholeNum))
print(wholeNum)

print(int(" 4321 "))

wholeNum2 = 123
wholeNum2 = float(wholeNum2)
print(wholeNum2)

float1 = float("98.76")
print(type(float1))
print(int)

print("Tekst z wartością " + str(wholeNum) + " oraz z listą " + str([1, 2, 3, 4, 5]))
print("Tekst z wartością", wholeNum, "oraz z listą ",[1, 2, 3, 4, 5])