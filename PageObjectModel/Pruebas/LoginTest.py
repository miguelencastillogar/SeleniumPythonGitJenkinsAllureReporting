import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# This module let me know all the directories' path that Python
# use to look for modules to import
#import sys

from Paginas.PaginaLogin import LoginPage
from Paginas.Pagina2 import Page2

class LoginTest(unittest.TestCase):

    def setUp(self):

        # We print all the path that Paytonh look for to import
        #------------------------------------------------------
        # print("\n")

        # for path in sys.path:
        #     print(f'{path}')
        #------------------------------------------------------
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/loginTest.html')

    def test_login_test(self):
        
        loginPage = LoginPage(driver)

        loginPage.login_page('Miguel', '123456')

        page2 = Page2(driver)

        page2.setText("Excelente")

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()