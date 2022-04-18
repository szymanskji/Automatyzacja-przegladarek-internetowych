import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFilter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def ilosc_gwiazdek(self, *gwiazdki):
        gw_box = self.driver.find_element_by_xpath('//*[@id="searchboxInc"]/div[1]/div/div/div[1]/div[6]')
        gw = gw_box.find_elements(By.CSS_SELECTOR, '*')

        for gwiazdka in gwiazdki:
            for _ in gw:
                if str(_.get_attribute('innerHTML')).strip() == f'{gwiazdka} gwiazdki' \
                        or str(_.get_attribute('innerHTML')).strip() == f'{gwiazdka} gwiazdek' \
                        or str(_.get_attribute('innerHTML')).strip() == f'{gwiazdka} gwiazdka':
                    self.driver.execute_script("arguments[0].click()", _)

    def najniższa_cena(self):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')
            self.driver.execute_script("arguments[0].click()", element)
        except selenium.common.exceptions.NoSuchElementException:
            element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
            self.driver.execute_script("arguments[0].click()", element)
            element =self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
            self.driver.execute_script("arguments[0].click()", element)
