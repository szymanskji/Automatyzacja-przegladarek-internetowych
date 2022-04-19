from booking.booking import Booking

with Booking() as bot:
    bot.odpalenie_strony()
    bot.waluta((input("Wprowadź walute: ")).upper())
    bot.miejsce(input("Wprowadź miasto: "))
    print("FORMAT DATY TO ROK-MIESIĄC-DZIEŃ")
    bot.termin(input("Wprowadź dzień zameldowania: "), input("Wprowadź dzień wymeldowania: "))
    while True:
        l_doroslych = int(input('Wprowadź liczbe osób: '))
        if 0 < l_doroslych <= 30:
            break
        else:
            print("NIEPRAWIDLOWA WARTOSC")
    bot.liczba_doroslych(l_doroslych)
    while True:
        l_pokoi = int(input('Wprowadź liczbe osób: '))
        if 0 < l_pokoi <= 30:
            break
        else:
            print("NIEPRAWIDLOWA WARTOSC")
    bot.liczba_pokoi(l_pokoi)
    bot.wyszukiwanie()
    bot.filtry(input("Wprowadź ilość gwiazdek: "))
    bot.refresh()
    bot.raport_hoteli()
    bot.teardown = True
