# Zadanie - zarządzanie książką adresową
# W tym zadaniu będziesz używać słowników do zarządzania prostą
# książką adresową. Nauczysz się dodawać, usuwać, kopiować oraz
# przeszukiwać dane w słowniku.
#
# 1) Stwórz słownik `addressBook` zawierający początkowo jedną
#    osobę: Jan Kowalski, mieszka w Gdańsku, kod pocztowy 80-000.
# 2) Dodaj do książki adresowej nową osobę: Anna Nowak, mieszka w
#    Warszawie, kod pocztowy 00-001.
# 3) Usuń Jan Kowalski z książki adresowej.
# 4) Skopiuj książkę adresową do nowej zmiennej i sprawdź, czy
#    kopia jest identyczna (porównaj referencje i zawartość).
# 5) Sprawdź, czy w skopiowanej książce adresowej jest osoba
#    mieszka w Krakowie. Jeśli nie, wyświetl odpowiedni komunikat.
# 6) Wyświetl wszystkie klucze i wartości w książce adresowej.

addressBook = {
    0 : {
        'name' : 'Jan',
        'surname' : 'Kowalski',
        'city' : 'Gdańsk',
        'postAddress' : '80-100',
    }
}

addressBook[1] = {
    'name' : 'Anna',
    'surname' : 'Nowak',
    'city' : 'Warszawa',
    'postAddress' : '00-001',
}

del addressBook[0]

adressBookCopy = addressBook.copy()
print(addressBook == adressBookCopy)
print(addressBook is adressBookCopy)

for key in addressBook.values():
    if key['city'] == 'Kraków':
        print("Osoba mieszka w Krakowie")
    else:
        print("Osoba nie mieszka w Krakowie")

print(addressBook)