# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

class SeleniumTest(unittest.TestCase):
    @unittest.skip("")
    def test_search_with_chrome(self):
        '''pruebas - SeleniumTest | La pagina contiene la palabra "python" '''
        browser = webdriver.Chrome()
        browser.get('http://www.python.org')
        self.assertEqual('Welcome to Python.org', browser.title)
        body = browser.find_element_by_css_selector('body')
        self.assertIn('python', body.text)