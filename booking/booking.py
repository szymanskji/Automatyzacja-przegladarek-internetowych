import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from booking.filtry import BookingFilter

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=chrome_options)
        self.implicitly_wait(15)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def odpalenie_strony(self):
        self.get("https://www.booking.com/index.pl.html")

    def waluta(self, Waluta):
        self.find_element(By.CSS_SELECTOR,
            'button[data-modal-header-async-type="currencyDesktop"]'
        ).click()
        element = self.find_element(By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={Waluta}"'
        )
        self.execute_script("arguments[0].click()", element)

    def miejsce(self, miasto):
        wyszukiwarka = WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.ID,"ss")))
        wyszukiwarka.clear()
        wyszukiwarka.send_keys(miasto)
        WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
            'li[data-i="0"]'
        ))).click()

    def termin(self, przyjazd, odjazd):
        element = self.find_element_by_css_selector(
            f'td[data-date="{przyjazd}"]'
        )
        self.execute_script("arguments[0].click()", element)
        element = self.find_element_by_css_selector(
             f'td[data-date="{odjazd}"]'
        )
        self.execute_script("arguments[0].click()", element)

    def liczba_doroslych(self, ilosc):
        self.find_element(By.ID,'xp__guests__toggle').click()
        d_ilosc1 = self.find_element(By.ID,'group_adults')
        while True:
            d_ilosc = d_ilosc1.get_attribute('value')
            if int(d_ilosc) == int(ilosc):
                break;
            if int(ilosc) < int(d_ilosc):
                element = WebDriverWait(self, 30).until(ec.element_to_be_clickable((By.XPATH,
                    '//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[1]'
                )))
                self.execute_script("arguments[0].click()", element)
            else:
                element = WebDriverWait(self, 30).until(ec.element_to_be_clickable((By.XPATH,
                    '//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[2]'
                )))
                self.execute_script("arguments[0].click()", element)

    def liczba_pokoi(self, ilosc):
        d_ilosc1 = self.find_element(By.ID, 'no_rooms')
        while True:
            d_ilosc = d_ilosc1.get_attribute('value')
            if int(d_ilosc) == int(ilosc):
                break;
            if int(ilosc) < int(d_ilosc):
                element = WebDriverWait(self, 30).until(ec.element_to_be_clickable((By.XPATH,
                    '//*[@id="xp__guests__inputs-container"]/div/div/div[4]/div/div[2]/button[1]'
                )))
                self.execute_script("arguments[0].click()", element)
            else:
                element = WebDriverWait(self, 30).until(ec.element_to_be_clickable((By.XPATH,
                    '//*[@id="xp__guests__inputs-container"]/div/div/div[4]/div/div[2]/button[2]'
                )))
                self.execute_script("arguments[0].click()", element)

    def wyszukiwanie(self):
        self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'
        ).click()

    def filtry(self):
        filtr = BookingFilter(driver=self)
        filtr.ilosc_gwiazdek(4, 5)
        filtr.najniższa_cena()
