import time
from tests.base_test import BaseTest
from pages.tecnicos import creacionTecnicos
from selenium.webdriver.common.by import By

class validar_picklist(BaseTest):
    def test_validar_opciones_picklist_especialidad(self):
        valores_esperados = ["Reparacion", "Instalacion", "Consulta"]

        tecnicos_page = creacionTecnicos(self.driver)
        tecnicos_page.abrir_modulo_tecnicos()
        tecnicos_page.abrir_formulario_nuevo()

        tecnicos_page.validar_opciones_picklist_seleccionables("Especialidad", valores_esperados)

        # (Opcional) Cierra el formulario
        tecnicos_page.cerrar_formulario()