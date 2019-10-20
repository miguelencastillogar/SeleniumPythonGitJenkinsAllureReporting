import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class ActionChain(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/')
        time.sleep(3)

    def test1_actionChain(self):

        # Cuando agregamos acciones del objeto ActionChains, las acciones
        # se guardan en memoria hasta se ejecuta el metodo perform() y las
        # acciones se ejecutan en el orden en que fueron agregadas,las acciones 
        # pueden ser agregadas en cadenas unas tras otras. Ejemplo:

        # ActionChains(driver).move_to_element(dropdown).click(opcionDinamica).perform()

        # 1-) Se mueve el raton hacia un dropdown.
        # 2-) Click en una de las opciones dinamicas desplegadas.
        # 3-) Se ejecuta e metodo perform() que ejecuta los pasos
        # 1 y2 en cadena.
        
        elemento = driver.find_element(By.XPATH, "//button[@class='dropbtn']")

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