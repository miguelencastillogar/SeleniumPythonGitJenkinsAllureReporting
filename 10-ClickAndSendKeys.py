import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndsendKeys(unittest.TestCase):

    def setUp(self):
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')
        time.sleep(3)

    def test_click_and_send_keys(self):        

        elemento = driver.find_element(By.XPATH, "//a[contains(text(), 'Pagina 2')]")

        if elemento is not None:

            elemento.click()

            elemento = driver.find_element(By.XPATH, "//input[@id='Segundo']")

            if elemento is not None:

                elemento.send_keys("Miguel Castillo")

            else:

                print('El elemento no fue encontrado')
            
        else:

            print('El elemento no fue encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()