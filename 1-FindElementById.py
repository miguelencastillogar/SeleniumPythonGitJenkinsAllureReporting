# Desde Selenium importamos el web driver
from selenium import webdriver

# ID: find_elemnt_by_id
# name: find_elemnt_by_name
# xpath: find_elemnt_by_xpath
# text: find_elemnt_by_link_text
# partial Text: find_elemnt_by_partial_link_text
# tagname: find_elemnt_by_tag_name
# class: find_elemnt_by_class_name
# css selector: find_elemnt_by_css_selector

# Creamos un driver que abrira Google Chrome
driver = webdriver.Chrome('Recursos\\chromedriver.exe')

# Maximizamos la ventana del Chrome
driver.maximize_window()

# Accedemos a la URL de prueba
driver.get('http://www.goodstartbooks.com/pruebas/index.html')

# Buscamos el elemento por su id
elemento = driver.find_element_by_id('noImportante')

# Mediante esta condicion verificamos si el elemento fue encontrado
if elemento is not None:
    print('El elemento fue encontrado')
else:
    print('El elemento no fue encontrado')

driver.quit()