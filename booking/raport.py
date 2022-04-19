import pyshorteners
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingRaport:
    def __init__(self, zbior: WebElement):
        self.zbior_okienek = zbior
        self.okienka = self.wybor_okienka()

    def wybor_okienka(self):
        return self.zbior_okienek.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pobierz_hotele(self):
        wyniki = []
        licznik = 1
        for okienko in self.okienka:
            nazwa = okienko.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').text
            try:
                ocena = okienko.find_element(By.XPATH, f"(//div[@class='b5cd09854e d10a6220b4'])[{licznik}]").text
            except:
                break
            cena = okienko.find_element(By.CSS_SELECTOR, 'span.fcab3ed991.bd73d13072').text
            odleglosc = okienko.find_element(By.CSS_SELECTOR, 'span[data-testid="distance"]').text
            strona = "booking.com"
            linkv1 = okienko.find_element(By.CSS_SELECTOR, 'a[data-testid="title-link"]').get_attribute('href')
            try:
                link = pyshorteners.Shortener().tinyurl.short(linkv1)
            except:
                pass
            wyniki.append(
                [nazwa, cena, ocena, odleglosc, strona, link]
            )
            licznik += 1
        return wyniki
