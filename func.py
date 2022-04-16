from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import threading

from websites import Websites


class My_Chrome(uc.Chrome):
    def __del__(self):
        pass
    
def main():
    sites = Websites()
    driver = My_Chrome()
    
if __name__ == '__main__':
    main()