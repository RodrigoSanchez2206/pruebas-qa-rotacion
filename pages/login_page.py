from selenium.webdriver.common.by import By
from utils.credentials import get_credentials

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self):
        username, password = get_credentials()
        self.driver.get("https://orgfarm-23b5231ee9-dev-ed.develop.my.salesforce.com/")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "Login").click()