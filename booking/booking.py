from time import sleep

import selenium
from prettytable import PrettyTable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from booking.filtry import BookingFilter
from booking.raport import BookingRaport


class Booking:
    def __init__(self, driver):
        self.driver = driver

    def odpalenie_strony(self):
        self.driver.get("https://www.booking.com/index.pl.html")

    def waluta(self, wal):
        while True:
            element = self.driver.find_element(By.CSS_SELECTOR,
                                        'button[data-modal-header-async-type="currencyDesktop"]'
                                        )
            self.driver.execute_script("arguments[0].click()", element)
            try:
                element = self.driver.find_element(By.CSS_SELECTOR,
                                            f'a[data-modal-header-async-url-param*="selected_currency={wal}"'
                                            )
                self.driver.execute_script("arguments[0].click()", element)
                break
            except selenium.common.exceptions.NoSuchElementException:
                wal = input("Wprowadź poprawnie walutę (zł = PLN): ")

    def miejsce(self, miasto):
        while True:
            wyszukiwarka = self.driver.find_element(By.ID, "ss")
            wyszukiwarka.clear()
            wyszukiwarka.send_keys(miasto)
            try:
                element = self.driver.find_element(By.CSS_SELECTOR,
                                            'li[data-i="0"]'
                                            )
                self.driver.execute_script("arguments[0].click()", element)
                break
            except selenium.common.exceptions.NoSuchElementException:
                miasto = input("Nie znaleziono takiego miasta. Możesz spróbować poszukać w innym mieście: ")

    def termin(self, przyjazd, odjazd):
        while True:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR,
                                            f'td[data-date="{przyjazd}"]'
                                            )
                self.driver.execute_script("arguments[0].click()", element)
                break
            except selenium.common.exceptions.NoSuchElementException:
                element = self.driver.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]')
                self.driver.execute_script("arguments[0].click()", element)
        while True:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR,
                                            f'td[data-date="{odjazd}"]'
                                            )
                self.driver.execute_script("arguments[0].click()", element)
                break
            except selenium.common.exceptions.NoSuchElementException:
                element = self.driver.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]')
                self.driver.execute_script("arguments[0].click()", element)

    def liczba_doroslych(self, ilosc):
        element = self.driver.find_element(By.ID, 'xp__guests__toggle')
        self.driver.execute_script("arguments[0].click()", element)
        d_ilosc1 = self.driver.find_element(By.ID, 'group_adults')
        while True:
            d_ilosc = d_ilosc1.get_attribute('value')
            if int(d_ilosc) == int(ilosc):
                break
            if int(ilosc) < int(d_ilosc):
                element = self.driver.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div['
                                                      '1]/div/div[2]/button[1]')
                self.driver.execute_script("arguments[0].click()", element)
            else:
                element = self.driver.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div['
                                                      '1]/div/div[2]/button[2]')
                self.driver.execute_script("arguments[0].click()", element)

    def liczba_pokoi(self, ilosc):
        d_ilosc1 = self.driver.find_element(By.ID, 'no_rooms')
        while True:
            d_ilosc = d_ilosc1.get_attribute('value')
            if int(d_ilosc) == int(ilosc):
                break
            if int(ilosc) < int(d_ilosc):
                element = self.driver.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div['
                                                      '4]/div/div[2]/button[1]')
                self.driver.execute_script("arguments[0].click()", element)
            else:
                element = self.driver.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div['
                                                      '4]/div/div[2]/button[2]')
                self.driver.execute_script("arguments[0].click()", element)

    def wyszukiwanie(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        self.driver.execute_script("arguments[0].click()", element)

    def filtry(self, lista):
        filtr = BookingFilter(driver=self.driver)
        if len(lista) == 0:
            filtr.najnizsza_cena()
        else:
            filtr.ilosc_gwiazdek(lista)
            filtr.najnizsza_cena()

    def odswiezenie_strony(self):
        self.driver.refresh()

    def raport_hoteli(self):
        okienka_hoteli = self.driver.find_element(By.ID, 'search_results_table')
        raport = BookingRaport(okienka_hoteli)
        tabela = PrettyTable(
            field_names=["NAZWA", "CENA", "OCENA", "ODLEGŁOŚĆ", "STRONA", "LINK"]
        )
        tabela.add_rows(raport.pobierz_hotele())
        print(tabela)
