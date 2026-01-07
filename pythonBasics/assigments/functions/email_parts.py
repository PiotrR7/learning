# String - zadanie:
# 1) Napisz funkcję getEmailParts przyjmującą
#    parametr email.
# 2) Wykorzystaj pobieranie fragmentów tekstu w python aby rozłożyć
#    email na części i zapisz je w zmiennych:
#    - user - od początku emaila do ostatniego znaku przed @
#    - domainName - tekst za @ i przed kropką
#    - domainExt - tekst za ostatnią kropką do końca
#    Uwaga: pamiętaj że określając początek i koniec fragmentu z stringa
#    możesz korzystać z zmiennych np:
#    monkeyInd = 5
#    user = email[0:monkeyInd]
# 3) Zwróć słownik z funkcji z elementami jak powyższe
#    zmienne. Pamiętaj aby użyć find aby określić
#    pozycję indeksu małpy w email, jeśli go nie ma
#    zwróć None z funkcji, podobnie z kropką.
# 4) Przetestuj funkcję na emailu:
#    ola@domena.com
#    W konsoli powinna pojawić się informacja:
#    {'user': 'ola', 'domainName': 'domena', 'domainExt': 'com'}

def getEmailParts(email):
    monkey = email.find('@')
    if monkey < 0: return None

    dot = email.rfind('.')
    if dot < 0: return None

    user = email[0:monkey]
    domainName = email[monkey + 1:dot]
    domainExt = email[dot + 1:]

    return {
        "user": user,
        "domainName": domainName,
        "domainExt": domainExt
    }

print(getEmailParts("ola@domena.com"))