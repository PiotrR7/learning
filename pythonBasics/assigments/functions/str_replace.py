# Zadanie String replace
# 1) Stwórz funkcję cleanText, która będzie czyścić
#    przekazany tekst z określonych słów.
# 2) Użyj funkcję replace do zamiany podanych słów na
#    wykropkowane, które wielokrotnie może pojawić się
#    w przekazanym łańcuchu. Dla uproszczenia będziesz
#    zamieniać nazwy języków programowania ;)  np.
#    php zmienisz na ***, java na **** itd
# 3) Zastąp następujące słowa kluczowe:
#    JavaScript, java, php, html, css
# 4) Zwróć wyczyszczony tekst z funkcji cleanText.
# 5) Wywołaj funkcję na następującym lub podobnym tekście:
#   """Programowanie zacząłem z językiem php, następnie
#    poznałem: html i css, ale obecnie skupiam się na
#    JavaScript"""
#    Wynik pokaż w konsoli.

text = """
    Programowanie zacząłem z językiem php, następnie
    poznałem: html i css, ale obecnie skupiam się na
    JavaScript.
"""

def cleanText(text):
    for el in ["php", "html", "css", "JavaScript", "java"]:
        if el in text:
            text = text.replace(el, "*" * len(el))
    return text

print(cleanText(text))