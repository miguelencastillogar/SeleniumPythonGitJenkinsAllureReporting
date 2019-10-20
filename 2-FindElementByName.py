from selenium import webdriver

driver = webdriver.Chrome('Recursos\\chromedriver.exe')
driver.maximize_window()
driver.get('http://www.goodstartbooks.com/pruebas/index.html')

elemento = driver.find_element_by_name('ultimo')

if elemento is not None:
    print('El elemento fue encontrado')
else:
    print('El elemento no fue encontrado')

driver.quit()