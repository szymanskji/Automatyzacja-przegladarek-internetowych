from booking.booking import Booking

with Booking() as bot:
    bot.odpalenie_strony()
    bot.waluta('PLN')
    bot.miejsce('Kraków')
    bot.termin(przyjazd='2022-04-21', odjazd='2022-04-25')
    bot.liczba_doroslych("5")
    bot.liczba_pokoi("2")
    bot.wyszukiwanie()
    bot.filtry()