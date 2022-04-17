from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List
class BookingFilter:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def gwiazdki(self, ilosc):
        filter_gwiazdki_box = self.driver.find_element(By.ID,'filter_class')
        filter_gwiazdki = filter_gwiazdki_box.find_element_by_css_selector('*')

        #for pom in filter_gwiazdki:
           # if str(pom.get_attribute('innerHTML')).strip() == f'{ilosc} '