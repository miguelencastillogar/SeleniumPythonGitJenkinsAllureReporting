from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CommonActions:
     
    def __init__(self, driver):
        
        self.driver = driver

    def verify_element_present_and_visible(self, element_present, element_visible, time_to_wait, locator, locator_value):

        try:
          
          # Time waiter
          waiter = WebDriverWait(self.driver, time_to_wait)

          # In case we just want verify element is present at the DOM
          if element_present and not element_visible:

               element = waiter.until(EC.presence_of_element_located((locator, locator_value)))

               if element is not None:

                    return True

          # In case we just want verify element is visible to user
          if not element_present and element_visible:

               element = waiter.until(EC.visibility_of((locator, locator_value)))

               if element is not None:

                    return True
          
          # In case we just want verify element is present at the DOPM and visible to the user
          if element_present and element_visible:

               element_visible = False
               
               element = waiter.until(EC.presence_of_element_located((locator, locator_value)))

               if element is not None:

                    element_visible = True
                    element_present = False

                    element = waiter.until(EC.visibility_of((locator, locator_value)))

                    if element is not None:

                         return True

        except:

          # In case we just want verify element is present at the DOM
          if element_present:
               print('\nEl emento no se encontraba presente en el DOM.')

          # In case we just want verify element is visible to user
          if element_visible:
               print('\nEl emento no se encontraba visible al usuario.')