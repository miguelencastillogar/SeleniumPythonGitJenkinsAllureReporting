import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickRadioButtonAndCheckBox(unittest.TestCase):

    def setUp(self):
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')
        time.sleep(3)

    def test1_click_radio_Buttton(self):        

        elemento = driver.find_element(By.XPATH, "//input[@id='RadioGroup1_0']")

        if elemento is not None:

            elemento.click()

            time.sleep(3)

            elemento = driver.find_element(By.XPATH, "//input[@id='RadioGroup1_1']")

            if elemento is not None:

                elemento.click()

                time.sleep(3)

            else:

                print('El elemento no fue encontrado')
            
        else:

            print('El elemento no fue encontrado')
    
    def test2_click_check_box(self):        

        elemento = driver.find_element(By.XPATH, "//input[@id='CheckboxGroup1_0']")

        if elemento is not None:

            elemento.click()

            time.sleep(5)

            elemento = driver.find_element(By.XPATH, "//input[@id='CheckboxGroup1_1']")

            if elemento is not None:

                elemento.click()

                time.sleep(5)

            else:

                print('El elemento no fue encontrado')
            
        else:

            print('El elemento no fue encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()