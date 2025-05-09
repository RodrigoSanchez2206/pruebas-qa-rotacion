from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.credentials import get_credentials

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Espera hasta que el campo 'username' esté presente
    
    def login(self):
        username, password = get_credentials()
        self.driver.get("https://orgfarm-23b5231ee9-dev-ed.develop.my.salesforce.com/")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "Login").click()

    def seleccionar_primer_contacto(self):
            # 1. Click en el input del combobox
            input_combobox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input.slds-combobox__input"))
            )
            input_combobox.click()

            # 2. Esperar a que aparezca el dropdown con opciones
            primer_resultado = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "lightning-base-combobox-item"))
            )

            # 3. Click en el primer resultado
            primer_resultado.click()