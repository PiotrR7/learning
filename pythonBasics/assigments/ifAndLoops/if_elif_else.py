"""
1. Stwórz zmienną number i przypisz jej wartośc 15
2. Sprawdź, czy number jest większe od 10. Jeśli tak, wyświetl komunikat.
3. Sprawdź, czy number jest równe 15. Jeśli tak wyświetl komunikat.
4. Użyj elif do sprawdzenia, czy number jest równe 20, 25, lub większe od 30.
    Dla każdego przypadku wyświetl odpowiedni komunikat
5. Jeśli żaden z powyższych warunków nie jest spełniony, użyl else do wyświetlenia
    domyślnego komunikatu.
6. Dodaj zagnieżdżoną instrukcję warunkową, aby sprawdzić dodatkowy warunek
    dla jednego z przypadków.
"""

number = 15

if number > 10:
    print("number > 10")

if number == 15:
    print("number == 15")
elif number == 20:
    print("number == 20")

    if number > 30:
        print("number > 30")
elif number == 25:
    print("number == 25")
else:
    print(number)