# Zadanie: Tworzenie profilu użytkownika
#
# Cel: Napisz program, który umożliwia utworzenie profilu użytkownika w systemie.
# Program powinien prosić użytkownika o podanie imienia, nazwiska, wieku oraz
# miasta pochodzenia. Nie wszystkie informacje są wymagane. Użyj funkcji z nazwanymi
# argumentami
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję createUserProfile przyjmującą argumenty: firstName, lastName,
#    age oraz city
# 2) Funkcja powinna zwracać słownik zawierający informacje o profilu użytkownika.
# 3) Poproś użytkownika o wprowadzenie wymaganych danych.
# 4) Wywołaj funkcję createUserProfile z odpowiednimi argumentami wprowadzonymi przez
#    użytkownika i przechowaj zwrócony słownik.
# 5) Wyświetl zwrócony profil użytkownika.

def createUserProfile(firstName, lastName, age, city):
    return {
        "firstName": firstName,
        "lastName": lastName,
        "age": age,
        "city": city
    }

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

userProfile = createUserProfile(firstName = firstName, lastName = lastName, age = age, city = city)
print(userProfile)