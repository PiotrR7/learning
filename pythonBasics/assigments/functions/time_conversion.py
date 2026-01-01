# Stwórz funkcje do konwersji czasu:
# 1) convertToSeconds przyjmująca ilość godzin
#    oraz minut i zwracająca ilość sekund.
#    Jako parametry funkcji zapisz: hours, minutes.
#    Skonwertuj 3 godziny i 25 minut na sekundy,
#    wynik pokaż w konsoli.
# 2) convertToHours przyjmującą parametr minutes
#    oraz zwracając ilość godzin.
#    Skonwertuj 120 minut na godziny i pokaż
#    wynik w konsoli.

def convertToSeconds(hours, minutes):
    return hours * 3600 + minutes * 60
print(convertToSeconds(3, 25))

def convertToHours(minutes):
    return minutes / 60
print(convertToHours(120))