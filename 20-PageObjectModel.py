import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from AcconesComunes.CommonAction import CommonActions

class ImplicitlyWait(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/loginTest.html')

    def test_login_and_navigation(self):
        
        commonActions = CommonActions(driver)

        commonActions.verify_element_present_and_visible(True, True, 3, By.XPATH, "//input[@id='nombre2']")
    
    def tearDown(self):
        
        driver.quit()

if __name__ == "__main__":
    unittest.main()