from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

class TecnicosDeServicioPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def abrir_modulo_tecnicos(self):
        # Esperar a que el botón de navegación esté presente y hacer clic
        nav_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show Navigation Menu']")))
        nav_button.click()

        # Esperar a que el enlace de técnicos de servicio esté presente y hacer clic
        tecnicos_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/lightning/o/Tecnico_de_Servicio__c/home']")))
        tecnicos_link.click()

    def abrir_formulario_nuevo(self):
        # Esperar a que el botón "Nuevo" esté presente y hacer clic
        nuevo_boton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='New']")))
        nuevo_boton.click()

    def llenar_formulario(self, nombre, apellido, especialidad, disponibilidad):
        # Nombre
        campo_nombre = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='Name']")))
        campo_nombre.send_keys(nombre)

    def obtener_especialidad(self):
        xpath = "//records-record-layout-item[@field-label='Especialidad']//lightning-formatted-text"
        especialidad_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        especialidad = especialidad_element.text
        print(f"[DEBUG] Especialidad del técnico: {especialidad}")
        return especialidad

