# Funkcje String:
# 1) Napisz funkcję getUserInformation z trzema parametrami:
#    name, surname, job
# 2) W getUserInformation zmień imię i nazwisko na duże litery,
#    zawód na małe, dodatkowo wyczyść te wartości
#    z białych znaków na ich początku i końcu
# 3) Połącz imię i nazwisko wraz z innym tekstem aby uzyskać tekst np:
#    "imię: ANIA, nazwisko: KOWALSKA, zawód: testerka"
# 4) Zwróć powstały tekst z funkcji
# 5) Wywołaj funkcję getUserInformation na następujących
#    danych i pokaż wynik w konsoli:
#    - Ania, Kowalska, Programistka
#    - Daniel, Lis, Administrator

def getUserInformation(name, surname, job):
    name = name.upper().strip()
    surname = surname.upper().strip()
    job = job.lower().strip()

    text = "Imię: {name}, nazwisko: {surname}, zawód: {job}".format(
        name = name,
        surname = surname,
        job = job
    )
    return text

print(getUserInformation(name = "Ania", surname = "Kowalska", job = "Programistka"))
print(getUserInformation(name = "Daniel", surname = "Lis", job = "Administrator"))