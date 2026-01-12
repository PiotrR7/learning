"""
1. Użyj modułu datetime, aby zapisać czas rozpoczęcia nad projektem
    jako zmienną start_time
2. Symuluj pracę nad projektem przez wywołanie time.sleep() z losowo
    wybranym krótkim czasem (np. od 1 do 5 sekund).
3. Użyj modułu datetime ponownie, aby zapisać czas zakończenia pracy
    nad projektem jako zmienną end_time
4. Oblicz łączny czas pracy nad projektem przez odjęcie start_time od end_time i wyświetl wynik
5. Jeśli łączny czas pracy przekracza 3 sekundy, wyświetl komunikat o dużej
    ilości włożonego czasu, w przeciwnym razie poinformuj o krótkim czasie pracy.
"""

import datetime
import time
import random

start_time = datetime.datetime(2026, 1, 12, 11, 51, 48)

time.sleep(random.randint(1, 5))

end_time = datetime.datetime.now()

duration = end_time - start_time
print("Czas pracy nad projektem: {time}".format(time = duration.total_seconds()))

if duration.total_seconds() > 3:
    print("Długi czas trwania projektu")
else:
    print("krótki czas trwania projektu")