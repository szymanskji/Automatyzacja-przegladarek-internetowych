from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class My_Chrome(uc.Chrome):
    def __del__(self):
        pass
    
def main():
    driver = My_Chrome()
    
    
if __name__ == '__main__':
    main()