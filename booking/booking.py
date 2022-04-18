import os
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from booking.filtry import BookingFilter
from booking.raport import BookingRaport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = Options()
        options.add_argument("--headless")
        ua = UserAgent()
        user_agent = ua.random
        options.add_argument(f'user-agent={user_agent}')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(chrome_options=options)
        self.set_window_size(1024, 600)
        options.add_argument("--headless")
        self.maximize_window()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def odpalenie_strony(self):
        self.get("https://www.booking.com/index.pl.html")

    def waluta(self, wal):
        self.find_element(By.CSS_SELECTOR,
                          'button[data-modal-header-async-type="currencyDesktop"]'
                          ).click()
        element = self.find_element(By.CSS_SELECTOR,
                                    f'a[data-modal-header-async-url-param*="selected_currency={wal}"'
                                    )
        self.execute_script("arguments[0].click()", element)

    def miejsce(self, miasto):
        wyszukiwarka = WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.ID, "ss")))
        wyszukiwarka.clear()
        wyszukiwarka.send_keys(miasto)
        element = WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                           'li[data-i="0"]'
                                                                           )))
        self.execute_script("arguments[0].click()", element)

    def termin(self, przyjazd, odjazd):
        element = self.find_element(By.CSS_SELECTOR,
                                    f'td[data-date="{przyjazd}"]'
                                    )
        self.execute_script("arguments[0].click()", element)
        element = self.find_element(By.CSS_SELECTOR,
                                    f'td[data-date="{odjazd}"]'
                                    )
        self.execute_script("arguments[0].click()", element)

    def liczba_doroslych(self, ilosc):
        element = self.find_element(By.ID, 'xp__guests__toggle')
        self.execute_script("arguments[0].click()", element)
        d_ilosc1 = self.find_element(By.ID, 'group_adults')
        while True:
            d_ilosc = d_ilosc1.get_attribute('value')
            if int(d_ilosc) == int(ilosc):
                break
            if int(ilosc) < int(d_ilosc):
                element = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div['
                                                      '1]/div/div[2]/button[1]')
                self.execute_script("arguments[0].click()", element)
            else:
                element = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div['
                                                      '1]/div/div[2]/button[2]')
                self.execute_script("arguments[0].click()", element)

    def liczba_pokoi(self, ilosc):
        d_ilosc1 = self.find_element(By.ID, 'no_rooms')
        while True:
            d_ilosc = d_ilosc1.get_attribute('value')
            if int(d_ilosc) == int(ilosc):
                break
            if int(ilosc) < int(d_ilosc):
                element = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div['
                                                      '4]/div/div[2]/button[1]')
                self.execute_script("arguments[0].click()", element)
            else:
                element = self.find_element(By.XPATH, '//*[@id="xp__guests__inputs-container"]/div/div/div['
                                                      '4]/div/div[2]/button[2]')
                self.execute_script("arguments[0].click()", element)

    def wyszukiwanie(self):
        element = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        self.execute_script("arguments[0].click()", element)

    def filtry(self):
        filtr = BookingFilter(driver=self)
        filtr.ilosc_gwiazdek(4, 5)
        filtr.najnizsza_cena()

    def raport_hoteli(self):
        okienka_hoteli = self.find_element(By.ID, 'search_results_table')
        raport = BookingRaport(okienka_hoteli)
        tabela = PrettyTable(
            field_names=["NAZWA", "CENA", "OCENA", "ODLEGŁOŚĆ"]
        )
        tabela.add_rows(raport.pobierz_hotele())
        print(tabela)
