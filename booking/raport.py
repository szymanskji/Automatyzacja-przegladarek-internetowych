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
            nazwa = okienko.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML')
            nazwa = nazwa.replace("&amp;", "&")
            temp = str(licznik)
            try:
                ocena = okienko.find_element(By.XPATH, "(//div[@class='b5cd09854e d10a6220b4'])[" + temp + "]").text
            except:
                break
            cena = okienko.find_element(By.CSS_SELECTOR, 'span.fcab3ed991.bd73d13072').get_attribute('innerHTML')
            cena = cena.replace(" ", "").replace("&nbsp;", " ")
            odleglosc = okienko.find_element(By.CSS_SELECTOR, 'span[data-testid="distance"]').get_attribute('innerHTML')
            wyniki.append(
                [nazwa, cena, ocena, odleglosc]
            )
            licznik = licznik +1
        return wyniki
