import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from booking.filtry import BookingFilter

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
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
        self.find_element(By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={Waluta}"'
        ).click()
    def miejsce(self,miasto):
        wyszukiwarka = WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.ID,"ss")))
        wyszukiwarka.clear()
        wyszukiwarka.send_keys(miasto)
        WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
            'li[data-i="0"]'
        ))).click()

    def termin(self, przyjazd, odjazd):
        self.find_element(By.CSS_SELECTOR,
            f'td[date-date="{przyjazd}"]'
        ).click()
        xxx = WebDriverWait(self, 15).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
            f'td[date-date="{odjazd}"]'
        )))
        xxx.click()

    def liczba_doroslych(self, ilosc):
        WebDriverWait(self, 5).until(ec.element_to_be_clickable((By.ID,'xp__guests__toggle'))).click()
        d_ilosc1 = self.find_element(By.ID,'group_adults')
        while True:
            d_ilosc = d_ilosc1.get_attribute('value')
            if int(d_ilosc) == int(ilosc):
                break;
            if int(ilosc) < int(d_ilosc):
               self.find_element_by_css_selector('//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[1]').click()
            else:
                self.find_element_by_css_selector('//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[2]').click()
    def wyszukiwanie(self):
        self.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'
        ).click()

    def filtry(self):
        filtr = BookingFilter(driver=self)
        filtr.gwiazdki()
