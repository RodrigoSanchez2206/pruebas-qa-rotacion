import time
from tests.base_test import BaseTest
from selenium.webdriver.common.by import By
from pages.panel_solicitudes_lwc_page import PanelSolicitudesLWC
from pages.solicitud_servicio_page import SolicitudServicioPage


class TestValidarSolcitudesActivas(BaseTest):


    def test_validar_solicitudes_activas(self):
        panel_page = PanelSolicitudesLWC(self.driver)
        panel_page.abrir_panel_solicitudes()
        panel_page.wait_for_component_to_load()
        estados = panel_page.get_lista_estados()
        for estado in estados:
            print(f"Estado encontrado: {estado}")
            self.assertNotEqual(estado.lower(), "cerrado", f"Se encontró una solicitud con estado inactivo: {estado}")

 