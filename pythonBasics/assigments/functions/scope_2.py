# Zadanie: Zarządzanie stanem konta użytkownika
#
# Cel: Napisz program do zarządzania stanem konta użytkownika, który pozwala na
# dodawanie i usuwanie środków oraz wyświetlanie aktualnego stanu konta. Program
# powinien korzystać z globalnej zmiennej do przechowywania stanu konta oraz
# zawierać funkcje do modyfikacji tego stanu i wyświetlania go.
#
# Kroki do wykonania:
# 1) Zdefiniuj globalną zmienną accountBalance z wartością początkową 0.
# 2) Napisz funkcję addFunds, która przyjmuje kwotę do dodania do konta.
#    Funkcja ta powinna modyfikować globalną zmienną accountBalance.
# 3) Napisz funkcję withdrawFunds, która przyjmuje kwotę do wypłaty z konta.
#    Sprawdź, czy stan konta pozwala na wypłatę - jeśli nie, wyświetl odpowiedni komunikat.
# 4) Napisz funkcję displayBalance, która wyświetla aktualny stan konta.
# 5) Zapytaj użytkownika w pętli o działanie (dodanie środków, wypłata, wyświetlenie stanu)
#    i odpowiednio zareaguj, wywołując odpowiednią funkcję.

accauntBalance = 0

def addFunds(amount):
    global accauntBalance
    accauntBalance += amount

def withdrawFunds(amount):
    global accauntBalance

    if amount > accauntBalance:
        return
    else:
        accauntBalance -= amount

def displayBalance(accauntBalance):
    print(accauntBalance)

while True:
    action = input("enter your choice:")
    if action == "brak": break
    if action == "dodanie środków":
        amount = int(input("enter amount:"))
        addFunds(amount)
    if action == "wypłata":
        amount = int(input("enter amount:"))
        withdrawFunds(amount)
    if action == "wyświetlenie stanu":
        displayBalance(accauntBalance)