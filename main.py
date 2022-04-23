import datetime
from multiprocessing import freeze_support
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from booking.booking import Booking
from fake_useragent import UserAgent

if __name__ == '__main__':
    freeze_support()
    options = Options()
    options.add_argument("--headless")
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    driver = uc.Chrome(options=options)
    options.add_argument("--headless")
    driver.maximize_window()
    driver.implicitly_wait(15)
    bot = Booking(driver)
    bot.odpalenie_strony()
    bot.waluta((input("Wprowadź walute: ")).upper())
    bot.miejsce(input("Wprowadź miasto: "))
    print("FORMAT DATY TO ROK-MIESIĄC-DZIEŃ")

    while True:
        przyjazd = input("Wprowadź dzień zameldowania: ")
        year, month, day = map(int, przyjazd.split('-'))
        try:
            date = datetime.date(year, month, day)
            dt = datetime.datetime.now()
            if date >= datetime.datetime.date(dt):
                break
            else:
                print("NIE MOŻESZ SZUKAĆ WSTECZ")
        except:
            print("NIEPRAWIDLOWA DATA")

    while True:
        odjazd = input("Wprowadź dzień wymeldowania: ")
        year, month, day = map(int, odjazd.split('-'))
        try:
            date = datetime.date(year, month, day)
            year, month, day = map(int, przyjazd.split('-'))
            if date > datetime.date(year, month, day):
                bot.termin(przyjazd, odjazd)
                break
            else:
                print("DZIEŃ WYMELDOWANIA NIE MOŻE BYĆ PRZESZŁY")
        except:
            print("NIEPRAWIDLOWA DATA")

    while True:
        l_doroslych = int(input('Wprowadź liczbe osób: '))
        if 0 < l_doroslych <= 30:
            bot.liczba_doroslych(l_doroslych)
            break
        else:
            print("NIEPRAWIDLOWA WARTOSC")

    while True:
        l_pokoi = int(input('Wprowadź liczbe pokoi: '))
        if 0 < l_pokoi <= 30:
            bot.liczba_pokoi(l_pokoi)
            break
        else:
            print("NIEPRAWIDLOWA WARTOSC")

    bot.wyszukiwanie()

    while True:
        gwiazdki = input("Wprowadź ilość gwiazdek: ")
        if gwiazdki != "":
            filtr = [1, 2, 3, 4, 5]
            lista = list(map(int, list(gwiazdki.split(' '))))
            result = [value for value in lista if value in filtr]
            if lista == result:
               bot.filtry(result)
               break
            else:
                print("NIEPRAWIDLOWA ILOSC GWIAZDEK (1-5)")
        else:
            bot.filtry(gwiazdki)
            break
    bot.odswiezenie_strony()
    bot.raport_hoteli()
