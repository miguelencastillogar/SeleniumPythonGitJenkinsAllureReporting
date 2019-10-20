import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class ChangeFocusToWindows(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/')
        time.sleep(3)

    def test1_change_focus_to_window(self):

        # Para cambiarse a otra pagina la clase web driver
        # ofrece las siguientes propiedades que accesan al
        # navegador:

        # current_url: URL de la pagina
        
        # current_window_handle: handle de la ventana actual,
        # handle es un numero de referencia manejado por el
        # sistema para cada ventana (cada ventana tiene un
        # handle o numero de referencia).
        
        # name: nombre del navegador
        
        # orientation: orientacion del dispositivo
        
        # page_source: codigo de la pagina
        
        # title: titulo de la pagina

        # window_handles: los handles de todas las ventanas
        # en la sesion actual

        # Para cambiarnos a una ventana, alerta o frame la clase WebDriver
        # ofrece los siguientes metodos:

        # switch_to.window()
        # switch_to.alert()
        # switch_to.frame()

        # Encuentra la ventana actual
        parentHandle = driver.current_window_handle
        print("Handle principal: ", parentHandle)

        elemento = driver.find_element(By.XPATH, "//input[@id='Buton1']")

        if elemento is not None:

            # Presionamos el boton Submit
            elemento.click()

            time.sleep(3)

            # Todos los handles
            todosHandles = driver.window_handles
            print("Todos los handles", todosHandles)

            # verificamos los handles y nos enfocamos en el que nos interesa
            for handle in todosHandles:

                if handle != parentHandle:

                    # Enfocamos nuestra ventana de interes
                    driver.switch_to.window(handle)

                    time.sleep(3)

                    elemento = driver.find_element(By.XPATH, "//input[@id='Segundo']")

                    if elemento is not None:

                        # Presionamos el boton Submit
                        elemento.send_keys("Miguel Castillo")

                        time.sleep(3)

                    else:
            
                        print("El elemento no fue encontrado")
        else:
            
            print("El elemento no fue encontrado")
    
    def tearDown(self):
        
        driver.quit()

if __name__ == "__main__":
    unittest.main()