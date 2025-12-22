# Zadanie: Wypisanie elementów z listy list
#
# Cel: Napisz program, który przechodzi przez zagnieżdżoną listę (listę list)
# i wypisuje wszystkie jej elementy.
#
# Kroki do wykonania:
# 1) Stwórz zmienną 'nested_list', która będzie zawierać kilka list z różnymi typami elementów.
# 2) Użyj zagnieżdżonej pętli for do przejścia przez wszystkie listy i ich elementy.
# 3) Wypisz każdy element z każdej listy.

nested_list = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    [True, False, None],
]

for element in nested_list:
    for item in element:
        print(item)