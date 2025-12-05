"""
1.Stwórz krotkę z ostatnimi wydatkami na koncie
    bankowym z wartościami: 100, 200, 300, 400, 500, 600
2.Policz wydatki za pomocą pętli for i wyświetl w konsoli
    ostateczną kwotę. Pamiętaj aby stworzyć zmienną
    z wartością początkową 0 do której dodasz kolejny wydatek
"""

expenses = (100, 200, 300, 400, 500, 600)

sum_expenses = 0
for expense in expenses:
    sum_expenses += expense