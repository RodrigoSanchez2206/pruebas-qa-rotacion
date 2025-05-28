# pages/creacion_de_productos.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class creacionProductos:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)