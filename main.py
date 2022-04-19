from time import sleep

from booking.booking import Booking

with Booking() as bot:
    bot.odpalenie_strony()
    bot.waluta((input("Wprowadź walute: ")).upper())
    bot.miejsce(input("Wprowadź miasto: "))
    print("FORMAT DATY TO ROK-MIESIĄC-DZIEŃ")
    bot.termin(input("Wprowadź dzień zameldowania: "), input("Wprowadź dzień wymeldowania: "))
    bot.liczba_doroslych(int(input('Wprowadź liczbe osób: ')))
    bot.liczba_pokoi(int(input('Wprowadź liczbe pokoi: ')))
    bot.wyszukiwanie()
    bot.filtry(input("Wprowadź ilość gwiazdek: "))
    bot.refresh()
    bot.raport_hoteli()
    bot.teardown = True