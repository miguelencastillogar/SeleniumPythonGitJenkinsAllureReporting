import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class GetAttributeAndText(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/')
        time.sleep(3)

    def test1_get_text(self):

        elemento = driver.find_element(By.XPATH, "//tr[@id='noImportante']/td[2]")

        if elemento is not None:

            # Obtenemos el texto del elemento
            print('El texto es: ', elemento.text)

        else:
            
            print("El elemento no fue encontrado")
        
        
        elemento = driver.find_element(By.XPATH, "//tr[@id='importante']")

        if elemento is not None:

            # Obtenemos el atributo del elemento
            print('El atributo class es: ', elemento.get_attribute('class'))

        else:
            
            print("El elemento no fue encontrado")
    
    def tearDown(self):
        driver.close()

if __name__ == "__main__":
    unittest.main()