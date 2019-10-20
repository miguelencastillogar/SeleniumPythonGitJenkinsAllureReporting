import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class ImplicitlyWait(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/')
        driver.implicitly_wait(15)

    def test1_implicitlyWait(self):

        # Webdriver espera por un tiempo maximo determinado,
        # para encontrar un elemento, tambien es el tiempo
        # de espera para que una instruccion termine

        # Solamente necesita ser llamado una sola vez por sesion

        # La configuracion funciona de manera general, la misma
        # cada vez que tratas de encontrar un elemento

        # Funciona durante la sesion, osea hasta que el webdriver
        # se cierre.
        
        # Esperar 15 segundos hasta encontrar el elemento
        elemento = driver.find_element(By.XPATH, "//button[@class='dropbtnn']")

        if elemento is not None:
            
            acciones = ActionChains(driver)
            acciones.move_to_element(elemento).perform()

            elemento = driver.find_element(By.LINK_TEXT, "Link 1")

            if elemento is not None:
                
                acciones.move_to_element(elemento)
                acciones.click()
                acciones.perform()

                time.sleep(3)

            else:
        
                print("El iframe no fue encontrado")

        else:
        
            print("El iframe no fue encontrado")
    
    def tearDown(self):
        
        driver.quit()

if __name__ == "__main__":
    unittest.main()