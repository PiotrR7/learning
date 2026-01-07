# String i find()
# 1) Napisz funkcję validateEmail sprawdzającą w podstawowy
#    sposób czy email jest prawidłowy.
# 2) Wykorzystaj find() do wyszukania fragmentów tekstu w email:
#    - sprawdź czy istnieje w przekazanym do funkcji emailu
#      znak @, zapisz index w monkeyIndex
#    - posiadając pozycję @ sprawdź czy istnieje znak
#      kropki po małpie. Zapisz pozycję kropki w dotIndex
#    - jeżeli wszystkie powyższe warunki są spełnione
#      zwróć True, w innym wypadku False
# 3) Wywołaj funkcję z następującymi mailami, pokaż
#    w konsoli co zwraca funkcja:
#    - asia@example.com
#    - karol@domena
#    - user.com

def validateEmail(email):
    monkeyIndex = email.find("@")
    if monkeyIndex < 0: return False

    dotIndex = email[monkeyIndex:].find(".")
    if dotIndex < 0: return False

    return True

print(validateEmail("asia@example.com"))
print(validateEmail("karol@domena"))
print(validateEmail("user.com"))