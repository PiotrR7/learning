
# pip install pytest
# uruchomienie testów to wywołanie po prostu "pytest" w terminalu

# Wprowadzenie:
# Pytest to framework do testowania kodu Python, umożliwiający pisanie prostych 
# oraz zaawansowanych testów.
# W tej lekcji dowiesz się, jak zainstalować Pytest, stworzyć podstawowy test, oraz uruchomić testy.
# Zacznijmy od instalacji Pytest za pomocą pip, a następnie przejdziemy 
# do tworzenia i uruchamiania prostego testu.


# Przykład funkcji do testowania i testu:

# Definicja prostej funkcji, którą będziemy testować
def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# Test sprawdzający poprawność działania funkcji `add`
def test_add():
    """Checks if the `add` function works correctly."""
    assert add(2, 3) == 5  # Verifies that adding 2 and 3 results in 5

# W test_add, używamy instrukcji assert do sprawdzenia, czy wynik działania funkcji add(2, 3) jest równy 5.
# Jeśli tak, test zostaje zaliczony. W przeciwnym razie, Pytest zgłosi błąd.

# Uruchamianie testów:
# Aby uruchomić testy, otwórz terminal w katalogu z plikami testowymi i wpisz `pytest`.
