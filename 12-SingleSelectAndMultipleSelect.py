import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class SingleSelectAndMultipleSelect(unittest.TestCase):

    # Para el elemento selec de html selenium proporcion
    # los siguientes metodos:

    # deselect_all(): en elementos de opcion multiple
    # remueve todas las selecciones.

    # deselect_by_index(index): remueve la seleccion
    # basandose en la posicion o indice.

    # deselect_by_value(value): remueve la seleccion
    # basandose en el valor de la seleccion.

    # deselect_by_visible_text(text): remueve la seleccion
    # basandose en el texto desplegado.

    # select_by_index(index): selecciona basandose
    # en la posicion o indice.

    # select_by_value(value): selecciona basandose
    # en el valor de la seleccion.

    # select_by_visible_text(text): selecciona basandose
    # en el texto desplegado.

    def setUp(self):
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')
        time.sleep(3)

    def test1_single_select_option(self):        

        elemento = driver.find_element(By.XPATH, "//select[@id='ingrediente']")

        if elemento is not None:

            single_dropdown = Select(elemento)
            single_dropdown.select_by_value('cebolla')

            time.sleep(3)
            
        else:

            print('El elemento no fue encontrado')
    
    def test2_multiple_select_option(self):

        elemento = driver.find_element(By.XPATH, "//select[@name='Select1']")

        if elemento is not None:

            multiple_dropdown = Select(elemento)
            multiple_dropdown.select_by_index(1)
            multiple_dropdown.select_by_visible_text('Sandia')

            time.sleep(3)

        else:

            print('El elemento no fue encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()