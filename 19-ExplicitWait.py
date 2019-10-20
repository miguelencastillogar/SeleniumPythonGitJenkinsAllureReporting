import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWait(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/')
        #driver.implicitly_wait(2)

    def test1_explicitWait(self):

        # En una espera explicita el webdriver define un tiempo
        # de espera para que ocurra una condicion especifica,
        # si la condicion se cuemple antes de terminar el tiempo
        # webdriver continua con el codigo y si la condicion no
        # ocurre en el tiempo determinado, un error ocurre.

        # expected_condition es la clase de selenium que contiene
        # las condiciones que pueden validarse con un espera explicita
        # y contiene los siguientes metodos:

        # element_to_be_clickable(): Espera por un elemento y revisa que
        # sea cisible y habilitado para darle click.

        # element_to_be_select(): espera a que el elemento se seleccione

        # presence_of__element_located(): Espera a que el elemento este
        #disponible en el DOM.

        # title_contains(): Espera que el titulo de la pagina contenga
        # un cadena de caracteres.
        
        # visibility_of(): localiza el elemento y espera que sea visible
        # y el tamaño del elemento sea mayor a cero.

        # text_to_be_present_in_element(): Localiza el elemento y espera
        # que contenga un texto.
        
        # alert_is_present(): Espera que una alerta exista.

        #Ejemplo:

        # WebDriverWait(self.driver, 10).ultil(expected_conditions.element_to_be_clickable((By.NAME, 'nameValue')))

        # 1-): WebDriverWait es la forma que Payton implementa esperas explicitas y
        # recibe como parametro el driver y numero (en este ejemplo 10) que especificara
        # el tiempo de espera en segundos para conseguir la condicion deseada.

        # 2-) continuando ultil que significa "espera" que recibe como parametro
        # la clase expected_condition y su metodo element_to_be_clickable y este
        # ultimo recibe como parametro la propiedad y el valor del elemento que
        # sera clickeado y debe ir entre parentesis adicionales para que sea tratado
        # como un solo parametro.

        espera = WebDriverWait(driver, 10)
        elemento = espera.until(EC.element_to_be_clickable((By.ID, "proceed")))

        if elemento is not None:
            
            elemento.click()

            time.sleep(3)

        else:
        
            print("El iframe no fue encontrado")
    
    def tearDown(self):
        
        driver.quit()

if __name__ == "__main__":
    unittest.main()