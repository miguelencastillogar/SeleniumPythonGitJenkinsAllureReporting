from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Page2:

    def  __init__(self, driver):

        self.driver = driver
    
    def setText(self, text):

        elemento = self.driver.find_element_by_id('Segundo')

        if elemento is not None:

            elemento.send_keys(text)
            
            time.sleep(3)