"""
1. Stwórz zmienną 'distance' z losową wartością od 100 do 1000, która
    oznacza dystans w kilometrach do pokonania.
2. Oblicz spodziewane spalanie na podróż, przyjmując, że na 100 km spala
    się 7 litrów paliwa. Użyj zaokrąglenia w górę.
3. Przyjmij cenę paliwa za litr jako losową wartość zmiennoprzecinkową
    między 4.5, a 5.5. Zaokrąlij cenę do dwóch miejsc po przecinku.
4. Oblicz całkowity koszt paliwa na podróż.
5. Jeśli koszt paliwa przekracza 400zł, wyświetl komunikat o wysokich
    kosztach podróży. W przeciwnym razie, poinformuj o przystępnych kosztach.
"""

import math
import random

distance = random.randint(100, 1000)

combustion = math.ceil(distance / 100 * 7)

fuelPrice = round(random.uniform(4.5, 5.5), 2)

travelPrice = round((combustion * fuelPrice), 2)

if travelPrice > 400:
    print("Wysokie koszty podróży. ", travelPrice)
else:
    print("Przystępne koszty podróży. ", travelPrice)