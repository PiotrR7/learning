"""
Zadanie: Kalkulator wieku psa na ludzkie lata
1. Poproś użytkownika o wprowadzenie wieku psa w latach i zapisz tę wartość do zmiennej.
2. Użyj instrukcji warunkowych, aby obliczyć wiek psa w ludzkich latach.
   - Pierwszy rok życia psa to 15 ludzkich lat. human_age = dog_age * 15
   - Drugi rok życia psa to kolejne 9 ludzkich lat. human_age = 15 + (dog_age - 1) * 9
   - Każdy kolejny rok to 5 ludzkich lat. 24 + (dog_age - 2) * 5
3. Jeśli podana wartość wieku psa jest mniejsza niż 0, wyświetl komunikat o błędzie.
4. Wyświetl wynik obliczeń w konsoli.
"""

dog_age = int(input("Wiek psa: "))
human_age = 0

if dog_age > 0:
    human_age += 15

    if dog_age >= 2:
        human_age += 9

        if dog_age >= 3:
            human_age += (dog_age - 2) * 5

    print("Wiek psa w latach ludzkich: ", str(human_age))
else:
    print("Błąd danych, wprowadzono wiek psa równy ", dog_age)