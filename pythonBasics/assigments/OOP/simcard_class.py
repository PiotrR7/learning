# Stwórz klasę SimCard reprezentującą kartę sim telefonu z kontaktami
# 1) Klasa ustawia atrybut/zmienną klasy contacts jako listę w konstruktorze
# 2) Dodaj metodę addContact przyjmującą oprócz self również parametry
#    name i telephone. Sprawdź z funkcją isinstance czy przekazane dane są
#    prawidłowe, czyli str i int. Stwórz słowik z name i telephone i dodaj go
#    do listy kontaktów obiektu powstałego na bazie klasy
# 3) Napisz metodę showContacts, która w pętli pokaże kolejne kontakty w terminalu
# 4) Stwórz instancję klasy SimCard
# 5) Dodaj poniższe kontakty:
#    - "Ola", 98765432
#    - "Adam", 12345678
#    - 100, 12345678
#    - "Kasia", "numer"
#    Część danych jest nieprawidłowa, więc nie powinny być dodane przez addContact
# 6) Wyświetl kontakty z showContacts()

class SimCard:
    def __init__(self) -> None:
        self.contacts = []

    def addContact(self, name, telephone):
        if isinstance(name, str) and isinstance(telephone, int):
            self.contacts.append({'name': name, 'telephone': telephone})

    def showContacts(self):
        for contact in self.contacts:
            print(f"{contact['name']}: {contact['telephone']}")

simCard = SimCard()
simCard.addContact(name = "Ola", telephone = 98765432)
simCard.addContact(name = "Adam", telephone = 12345678)
simCard.addContact(name = 100, telephone = 12345678)
simCard.addContact(name = "Kasia", telephone = "number")
simCard.showContacts()