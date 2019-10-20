# unittest — Unit testing framework

# (If you are already familiar with the basic concepts of testing,
# you might want to skip to the list of assert methods.)

# The unittest unit testing framework was originally inspired by JUnit
# and has a similar flavor as major unit testing frameworks in other
# languages.It supports test automation, sharing of setup and shutdown
# code for tests, aggregation of tests into collections, and independence
# of the tests from the reporting framework.

# To achieve this, unittest supports some important concepts
# in an object-oriented way:

# test fixture
# A test fixture represents the preparation needed to perform one
# or more tests, and any associate cleanup actions. This may involve,
# for example, creating temporary or proxy databases, directories,
# or starting a server process.

# test case
# A test case is the individual unit of testing. It checks for a specific
# response to a particular set of inputs. unittest provides a base class,
# TestCase, which may be used to create new test cases.

# test suite
# A test suite is a collection of test cases, test suites, or both.
# It is used to aggregate tests that should be executed together.

# test runner
# A test runner is a component which orchestrates the execution
# of tests and provides the outcome to the user. The runner may
# use a graphical interface, a textual interface, or return
# a special value to indicate the results of executing the tests.

# Esto es necesario para convertir este script en Unittest
import unittest
# Desde Selenium importamos el web driver
from selenium import webdriver

# Luego de importa el web driver de selenium
# nuestra clase de  prueba que llevara el nombre
# que deseemos tiene que heredar de Unit Test Class.
class FindByIdName(unittest.TestCase):

    # Necesitamos creo dos metodos que hacen
    # referencia al concepto Test Fixture de
    # UnitTest.

    # TestFixture setUp(self) y este es el punto
    # de entrada en donde agregamos las pre-
    # condiciones del caso de prueba.
    def setUp(self):
        
        # Especificamos que la variable driver sera global
        global driver
        driver = webdriver.Chrome('Recursos\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://www.goodstartbooks.com/pruebas/index.html')

    # Las validaciones de nuestras pruebas debemos
    # agregarlas en un metodo, de hecho podemos nombrar
    # nombrar el metodo como deseemos, tomando en cuenta
    # que en Unittest debe empezar con la palabra "test"
    def testIdName(self):

        elemento = driver.find_element_by_name('ultimo')

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

        elemento = driver.find_element_by_id('noImportante')

        if elemento is not None:
            print('El elemento fue encontrado')
        else:
            print('El elemento no fue encontrado')

    # TestFixture tearDown(self) y este es
    # el punto final donde agregamos las post-
    # condiciones del caso de prueba.
    def tearDown(self):
        driver.quit()

# Es una fomra estandar en Python para asegurarse
# que este unittest esta corriendo como programa
# independiente y no es llamado desde otro modulo.
# generalmente no es necesario si no sera llamado
# desde otro modulo
if __name__ == "__main__":
    # unittest.main() va a ejecutar setUp(), nuestra pruebas
    # y tearDown().
    unittest.main()