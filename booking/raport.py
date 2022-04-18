from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingRaport:
    def __init__(self, okienko:WebElement):
        self.okienko = okienko
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.okienko.find_elements(By.CSS_SELECTOR,
            'div[data-testid="property-card"]'
        )

    def pull_titles(self):
        wyniki = []
        for deal_box in self.deal_boxes:
            nazwa = deal_box.find_element(By.CSS_SELECTOR,
                'div[data-testid="title"]').get_attribute('innerHTML').strip()
            nazwa = nazwa.replace("&amp;", "&")
            ocena = deal_box.find_element(By.CSS_SELECTOR,
                'div.b5cd09854e.d10a6220b4').get_attribute('innerHTML').strip()
            cena = deal_box.find_element(By.CSS_SELECTOR,
                'span.fcab3ed991.bd73d13072').get_attribute('innerHTML').strip()
            cena = cena.replace(" ","").replace("&nbsp;"," ")
            odleglosc = deal_box.find_element(By.CSS_SELECTOR,
                'span[data-testid="distance"]').get_attribute('innerHTML').strip()

            wyniki.append(
                [nazwa, cena, ocena, odleglosc]
            )

        return wyniki