import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):

    def setUp(self):
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')

    def testTagName(self):

        # Aunque aparezcan mas de un elemento, siempre nos
        # dara el primero encontrado
        elemento = driver.find_element_by_tag_name("a")

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

    def testCssSelector(self):

        elemento = driver.find_element_by_css_selector('#form1')

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()