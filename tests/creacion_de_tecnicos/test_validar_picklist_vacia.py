import time
from tests.base_test import BaseTest
from pages.tecnicos import creacionTecnicos
from selenium.webdriver.common.by import By

class validar_picklist_vacia(BaseTest):
    def test_validar_picklist_vacia(self):
        tecnicos_page = creacionTecnicos(self.driver)
        tecnicos_page.abrir_modulo_tecnicos()
        tecnicos_page.abrir_formulario_nuevo()

        # Llenar el formulario dejando el nombre vacío
        tecnicos_page.validar_error_picklist(
            nombre="Johan",
            apellido="Garcia",
            especialidad="--None--"
        )