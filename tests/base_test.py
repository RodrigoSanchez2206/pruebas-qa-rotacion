import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        LoginPage(self.driver).login()

    def tearDown(self):
        self.driver.quit()
