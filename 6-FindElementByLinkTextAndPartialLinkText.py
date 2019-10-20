import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):

    def setUp(self):
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')

    def testLinkText(self):

        elemento = driver.find_element_by_link_text("Pagina 2")

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

    def testPartialLinkText(self):

        elemento = driver.find_element_by_partial_link_text('agina')

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()