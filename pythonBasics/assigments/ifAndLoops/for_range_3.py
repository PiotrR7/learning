# Zadanie: Wypisywanie liczb parzystych i nieparzystych
#
# Cel: Napisz program, który dla podanego zakresu od 1 do N (gdzie N jest
# wartością wprowadzoną przez użytkownika) wypisze oddzielnie listy liczb
# parzystych i nieparzystych.
#
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie liczby N, która określi zakres.
# 2) Użyj pętli for wraz z funkcją range() do iteracji od 1 do N włącznie.
# 3) Sprawdź za pomocą instrukcji warunkowej, czy aktualna liczba jest parzysta czy nieparzysta.
# 4) Dodaj liczby parzyste do jednej listy, a nieparzyste do drugiej, możesz stosoować append()
# 5) Po zakończeniu iteracji wyświetl obie listy: listę liczb parzystych i listę liczb nieparzystych.

N = int(input("N: "))
oddNumbers = []
evenNumbers = []

for x in range(1, N+1):
    if x % 2 == 0:
        evenNumbers.append(x)
    else:
        oddNumbers.append(x)

print(evenNumbers)
print(oddNumbers)