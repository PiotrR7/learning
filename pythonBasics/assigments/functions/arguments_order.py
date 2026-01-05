# Zadanie: Rezerwacja biletów na koncert
#
# Cel: Napisz program, który pozwoli użytkownikowi zarezerwować bilety na koncert.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję bookTickets, która przyjmuje nazwę zespołu jako argument
#    pozycyjny (band), liczbę biletów jako argument pozycyjny, a rodzaj biletów i sekcję
#    jako argumenty nazwane z domyślnymi wartościami jako standard i general
# 2) Funkcja powinna wyświetlać informacje o rezerwacji, włączając w to wszystkie
#    podane detale.
# 3) Poproś użytkownika o wprowadzenie nazwy zespolu i liczby bieltów,
#    następnie tylko je przekaż przy wywołaniu funkcji.

def bookTickets(band, ticketsCount, /, *, ticketType = "standard", section = "general"):
    print([band, ticketsCount, ticketType, section])

band = input("Enter a band of your choice: ")
ticketsCount = int(input("Enter a number of tickets: "))

bookTickets(band, ticketsCount)