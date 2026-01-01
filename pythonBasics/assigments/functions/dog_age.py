# Zadanie: Kalkulator wieku psa w ludzkich latach
#
# Cel: Napisz program, który przelicza wiek psa na ludzkie lata. Program powinien prosić użytkownika
# o wprowadzenie wieku psa, a następnie obliczyć i wyświetlić jego wiek w ludzkich latach.
# Pierwsze dwa lata życia psa liczymy jako 10.5 ludzkiego roku za każdy, a każdy kolejny
# rok jako 4 ludzkie lata.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję calculateHumanYears, która przyjmuje wiek psa jako parametr.
#    W funkcji użyj instrukcji if-elif-else do obliczenia wieku psa w ludzkich latach.
#    Dla uproszczenia załóżmy że ilość lat mniejsza równa 2 musi być pomnożona przez 10.5,
#    a dla większych wartości od 2 trzeba zastosować działanie  21 + (dogYears - 2) * 4
# 2) Użyj pętli, aby umożliwić użytkownikowi wielokrotne używanie kalkulatora bez
#    restartowania programu.
# 3) Poproś użytkownika o wprowadzenie wieku psa.
# 4) Wywołaj funkcję calculateHumanYears i przekaż jej wiek psa wprowadzony przez użytkownika.
# 5) Wyświetl obliczony wiek psa w ludzkich latach.

def calculateHumanYears(age):
    humanYears = 0
    if age <= 2:
        humanYears = age * 10.5
    elif age > 2:
        humanYears = 21 + (age - 2) * 4

    return humanYears

while True:
    age = float(input("Enter dog age: "))
    if age <= 0:
        break

    print(calculateHumanYears(age))