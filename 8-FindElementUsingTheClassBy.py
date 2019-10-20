import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName(unittest.TestCase):

    def setUp(self):
        
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')

    def testFindElementUsingTheClassBy(self):

        # driver.find_element(By.ID, 'id')
        # driver.find_element_by_id('id')

        # driver.find_element(By.XPATH, 'xpath')
        # driver.find_element_by_xpath('xpath')

        # driver.find_element(By.LINK_TEXT, 'text')
        # driver.find_element_by_link_text('text')

        # driver.find_element(By.PARTIAL_LINK_TEXT, 'partialLinkText')
        # driver.find_element_by_partial_link_text('partialLinkText')

        # driver.find_element(By.NAME, 'name')
        # driver.find_element_by_name('name')

        # driver.find_element(By.TAG_NAME, 'tagName')
        # driver.find_element_by_tag_name('tagname')

        # driver.find_element(By.CLASS_NAME, 'className')
        # driver.find_element_by_class_name('className')

        # driver.find_element(By.CSS_SELECTOR, 'cssSelector')
        # driver.find_element_by_css_selector('cssSelector')

        elemento = driver.find_element(By.XPATH, "//tr[@id='noImportante']")

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()