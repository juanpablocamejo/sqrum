import unittest
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):
    def testSearhWithFirefox(self):
        browser = webdriver.Firefox()
        browser.get('http://www.python.org')
        self.assertEqual('Welcome to Python.org', browser.title)
        body = browser.find_element_by_css_selector('body')
        self.assertIn('python', body.text)
    def testSearhWithChrome(self):
        browser = webdriver.Chrome()
        browser.get('http://www.python.org')
        self.assertEqual('Welcome to Python.org', browser.title)
        body = browser.find_element_by_css_selector('body')
        self.assertIn('python', body.text)