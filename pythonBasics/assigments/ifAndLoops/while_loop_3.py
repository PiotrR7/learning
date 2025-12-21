# Zadanie: Obliczanie średniej arytmetycznej
#
# Cel: Napisz program, który oblicza średnią arytmetyczną z podanej przez użytkownika
# listy liczb. Program powinien prosić użytkownika o wprowadzenie liczby elementów
# do obliczenia średniej, a następnie o wprowadzenie każdej z tych liczb.

# Kroki do wykonania:
# 1. Poproś użytkownika o wprowadzenie liczby elementów, z których ma być obliczona średnia.
# 2. Zainicjuj zmienną 'sum' wartością 0, która będzie przechowywać sumę wprowadzonych liczb.
# 3. Użyj pętli while do pobrania od użytkownika określonej liczby elementów. Po wprowadzeniu
#    każdej liczby dodaj ją do zmiennej 'sum'.
# 4. Oblicz średnią arytmetyczną, dzieląc sumę przez liczbę elementów.
# 5. Wyświetl wynikową średnią arytmetyczną z dokładnością do dwóch miejsc po przecinku.
# 6. Jeśli użytkownik wprowadzi liczbę elementów równą 0, wyświetl informację, że nie można
#    obliczyć średniej z 0 elementów.

sum = 0
numberOfRepeats = float(input("Ile chcesz podać liczb?: "))
operationsCounter = numberOfRepeats

if numberOfRepeats <= 0:
    print("Nie można obliczyć średniej z 0 elementów.")
else:
    while operationsCounter >= 1:
        sum += float(input("Podaj liczbę: "))
        operationsCounter -= 1

print("Średnia arytmetyczna: ", (sum/numberOfRepeats))
