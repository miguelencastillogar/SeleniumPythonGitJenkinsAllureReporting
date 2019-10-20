from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:

    def __init__(self, driver):

        self.driver = driver

    def login_page(self, username, password):
       
       elemento = self.driver.find_element_by_id('nombre')
       
       if elemento is not None:
           
           elemento.send_keys(username)

           elemento = self.driver.find_element_by_id('contrasena')

           if elemento is not None:

               elemento.send_keys(password)

               time.sleep(3)
               
               elemento = self.driver.find_element_by_id('proceed')

               if elemento is not None:
                   
                   elemento.click()

                   time.sleep(3)