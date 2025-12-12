"""
1.Stwórz zmienna config która bedzie słownikiem
    z konfiguracją strony internetowej, zapisz w niej poniższe
    klucze z wartością:
        - "website" z wartością "example.com"
        - "dbType" z wartością "mysql"
        - "dbUser" z wartością "admin"
        - "dbPassword" z wartością "12345"
2.Pokaż ilość elementów słownika w konsoli
3.Pokaż w konsoli wartośc klucza "dbType" z słownika
4.Wykorzystaj pętle for in aby przejść po wszystkich
    elementach słownika i pokaż je w konsoli według foramtu:
        "Klucz w config: website z wartością example.com"
"""

config = {
    "website": "example.com",
    "dbType": "mysql",
    "dbUser": "admin",
    "dbPassword": "12345",
}

print(len(config))
print(config["dbType"])

for key, value in config.items():
    print("Klucz w config: ", key, " z wartością ", value)