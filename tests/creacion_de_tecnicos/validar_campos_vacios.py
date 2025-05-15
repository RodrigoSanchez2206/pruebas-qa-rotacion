import time
from tests.base_test import BaseTest
from pages.tecnicos import creacionTecnicos
from selenium.webdriver.common.by import By

class validar_campos(BaseTest):
    def test_validar_que_formulario_no_se_guarde_con_campos_vacios(self):
        tecnicos_page = creacionTecnicos(self.driver)
        tecnicos_page.abrir_modulo_tecnicos()
        tecnicos_page.abrir_formulario_nuevo()

        # No llenar ningún campo, solo intentar guardar
        tecnicos_page.validar_error_por_campos_vacios()
