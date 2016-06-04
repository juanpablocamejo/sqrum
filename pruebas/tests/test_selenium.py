import unittest
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):
    def testMethod(self):
        browser = webdriver.Firefox()
        browser.get('http://www.python.org')
        self.assertEqual('Welcome to Python.org', browser.title)
        body = browser.find_element_by_css_selector('body')
        self.assertIn('python', body.text)
