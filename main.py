from booking.booking import Booking

with Booking() as bot:
    bot.odpalenie_strony()
    #bot.waluta('USD')
    bot.miejsce('Kraków')
   # bot.termin(przyjazd='2022-04-17',odjazd='2022-04-18')
    bot.liczba_doroslych("5")
    bot.wyszukiwanie()