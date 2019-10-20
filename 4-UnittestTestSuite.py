import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):

    def setUp(self):
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')

    # Este metodo se ejecutara como el primer caso de prueba,
    # se ejecutaran es SetUp(self) y el tearDown(self) para
    # este caso unicamente.
    def testId(self):

        elemento = driver.find_element_by_name('ultimo')

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

    # Este metodo se ejecutara como el segundo caso de prueba,
    # se ejecutaran es SetUp(self) y el tearDown(self) para
    # este caso unicamente, luego de finalizar el primer caso
    # testId(self).
    def testName(self):

        elemento = driver.find_element_by_id('noImportante')

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()