import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class HandlingAlert(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/')
        time.sleep(3)

    def test1_handling_alert(self):

        elemento = driver.find_element(By.XPATH, "//div[@id='center']/button")

        if elemento is not None:

            elemento.click()

            time.sleep(3)

            alerta = driver.switch_to.alert

            alerta.accept()

            time.sleep(3)

        else:
            
            print("El elemento no fue encontrado")
    
    def tearDown(self):
        
        driver.quit()

if __name__ == "__main__":
    unittest.main()