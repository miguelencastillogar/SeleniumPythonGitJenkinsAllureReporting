import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import pytest
import allure

class ChangeFocusToFrame(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/')
        time.sleep(5)

    def test1_change_focus_to_frame(self):

        # Encontramos el elemento frame
        iframe = driver.find_element(By.XPATH, "//iframe[@id='pruebas-iframe']")

        if iframe is not None:
            
            # Cambiamos el foco al frame
            driver.switch_to.frame(iframe)

            elemento = driver.find_element(By.XPATH, "//input[@id='Segundo']")

            if elemento is not None:

                elemento.send_keys('Miguel Castillo')

                time.sleep(3)

            else:
                
                print("El elemento no fue encontrado")

        else:
            
            print("El iframe no fue encontrado")
    
    def tearDown(self):
        
        driver.quit()

if __name__ == "__main__":
    unittest.main()

# class DemoAllure(unittest.TestCase):

#     def test_site_loads(self):
#         with pytest.allure.step("Launch site"):
#             driver = webdriver.Chrome()
#             driver.get("http://qaboy.com/")
#         with pytest.allure.step("Verify Title loaded"):
#             wait = WebDriverWait(driver, 5)
#             wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")


# class DemoAllure(unittest.TestCase):

#     def test_site_loads(self):
#         self.launch_site()
#         self.verify_site()

#     @pytest.allure.step("Launch site")
#     def launch_site(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://qaboy.com/")

#     @pytest.allure.step("Verify Title loaded")
#     def verify_site(self):
#         wait = WebDriverWait(self.driver, 5)
#         wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))