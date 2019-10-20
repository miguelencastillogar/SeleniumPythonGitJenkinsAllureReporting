import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName(unittest.TestCase):

    def setUp(self):
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')

    def testFindElementsUsingTheClassBy(self):

        # driver.find_elements(By.ID, 'id')
        # driver.find_elements_by_id('id')

        # driver.find_elements(By.XPATH, 'xpath')
        # driver.find_elements_by_xpath('xpath')

        # driver.find_elements(By.LINK_TEXT, 'text')
        # driver.find_elements_by_link_text('text')

        # driver.find_elements(By.PARTIAL_LINK_TEXT, 'partialLinkText')
        # driver.find_elements_by_partial_link_text('partialLinkText')

        # driver.find_elements(By.NAME, 'name')
        # driver.find_elements_by_name('name')

        # driver.find_elements(By.TAG_NAME, 'tagName')
        # driver.find_elements_by_tag_name('tagname')

        # driver.find_elements(By.CLASS_NAME, 'className')
        # driver.find_elements_by_class_name('className')

        # driver.find_elements(By.CSS_SELECTOR, 'cssSelector')
        # driver.find_elements_by_css_selector('cssSelector')

        # Todos los metodos descritos arriba no devuelven
        # una lista, que no es mas que la cantidad de elementos
        # encontrados con la misma caracteristica con la cual hicimos
        # la busqueda.

        # Buscaremos todas las filas de una tabla
        filas = driver.find_elements(By.XPATH, "//tr")

        if filas is not None:

            # la funcion len() te regresa cuantos
            # elementos existen en una lista
            cantidad_filas = len(filas)

            print(f'\n{cantidad_filas} elementos')
            
        else:

            print('El elemento no fue encontrado')

    def testFindElementsUsingTheClassByTagName(self):

        # Buscaremos todos los tag tr
        filas = driver.find_elements(By.TAG_NAME, "tr")

        if filas is not None:

            cantidad_filas = len(filas)

            print(f'\n{cantidad_filas} elementos')
            
        else:

            print('El elemento no fue encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()