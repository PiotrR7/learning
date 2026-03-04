# Wprowadzenie:
# Parametryzacja testów w Pytest pozwala na uruchomienie tego samego testu z różnymi zestawami danych.
# Jest to szczególnie użyteczne, gdy chcemy przetestować funkcję z różnymi wartościami wejściowymi.
# W tej lekcji nauczymy się, jak używać parametryzacji w Pytest.

import pytest

# Przykład funkcji do testowania
def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

# Użycie parametryzacji w Pytest do testowania funkcji `multiply` z różnymi zestawami 
# danych
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),  # Test case 1: 2 * 3 = 6
    (3, 7, 21),  # Test case 2: 3 * 7 = 21
    (5, 5, 25),  # Test case 3: 5 * 5 = 25
    (0, 4, 0)    # Test case 4: 0 * 4 = 0
])
def test_multiply(x, y, expected):
    """Checks if the `multiply` function works correctly with different sets of inputs."""
    assert multiply(x, y) == expected  # Verifies that multiply(x, y) results in expected output

# W funkcji test_multiply, parametry `x`, `y` i `expected` są wartościami, które 
# będą różne dla każdego zestawu danych.
# Dekorator @pytest.mark.parametrize jest używany do określenia zestawów danych 
# (parametrów testowych) oraz oczekiwanych wyników.
# Dla każdego zestawu danych, Pytest automatycznie generuje i wykonuje test.

