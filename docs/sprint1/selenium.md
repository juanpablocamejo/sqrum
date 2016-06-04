**Resultado del spike**

Selenium

Es un framework para automatizar test de UI, 
que hace uso de los navegadores web, es decir, 
un modulo llamado driver, levanta el ejecutable del navegador,
por ej "chrome", y luego lo controla, enviandole instrucciones de
las acciones a realizar en el navegador.
Estas acciones pueden ser practicamente cualquier cosa que pueda **hacer** un humano
con el browser: abrir paginas, clickear botones, agregar texto en un campo, esperar a que se
cargue una página, 
y tambien **verificar** cosas del estilo de:
Si existe un texto en un campo, si existe una opción en un combobox,
en fin.
por ultimo, para distintos lenguajes de programación, 
hay librerías para bindear con la api de selenium.
por lo tanto, uno puede escribir un test de python, haciendo uso de selenium.
Este es un ejemplo:
```python
class PythonOrgSearch(unittest.TestCase):
    
def testMethod(self):
        browser = webdriver.Firefox()
        browser.get('http://www.python.org')
        self.assertEqual('Welcome to Python.org', browser.title)
        body = browser.find_element_by_css_selector('body')
        self.assertIn('python', body.text)
```
