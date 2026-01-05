# Zadanie: Przetwarzanie danych użytkowników
# Cel: Napisz program do przetwarzania danych użytkowników z listy.
#
# Kroki do wykonania:
# 1) Stwórz listę słowników users, gdzie każdy słownik zawiera klucze 'name' i 'age'
#    z przykładowymi danymi użytkowników.
# 2) Użyj filter do wyfiltrowania użytkowników, którzy mają więcej niż 18 lat.
# 3) Użyj map do podwojenia wieku przefiltrowanych użytkowników.
# 4) Użyj reduce do zsumowania wszystkich lat po przetworzeniu.
# 5) Wyświetl sumę lat przefiltrowanych i przetworzonych użytkowników.
#
# Rozwiązanie:

from functools import reduce

# Przykładowa lista użytkowników
users = [
    {'name': 'Jan', 'age': 15},
    {'name': 'Anna', 'age': 25},
    {'name': 'Piotr', 'age': 30},
    {'name': 'Katarzyna', 'age': 22}
]

adults = list(filter(lambda user: user['age'] >= 18, users))
print(adults)

doubleAge = list(map(lambda user: user['age'] * 2, adults))
print(doubleAge)

sum = reduce(lambda x, y: x + y, doubleAge)
print(sum)