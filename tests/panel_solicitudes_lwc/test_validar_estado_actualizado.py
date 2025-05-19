import time
from tests.base_test import BaseTest
from selenium.webdriver.common.by import By
from pages.panel_solicitudes_lwc_page import PanelSolicitudesLWC
from pages.solicitud_servicio_page import SolicitudServicioPage


class TestValidarEstadoActualizado(BaseTest):

   def test_validar_estado_actualizado(self):
        solicitud_page = SolicitudServicioPage(self.driver)
        solicitud_page.abrir_modulo_solicitudes()
        solicitud_page.entrar_a_solicitud()
        nombre_solicitud = solicitud_page.actualizar_estado("Abierto")  
        panel_page = PanelSolicitudesLWC(self.driver)
        panel_page.abrir_panel_solicitudes()
        panel_page.wait_for_component_to_load()
        estado_obtenido = panel_page.get_estado(nombre_solicitud)
        assert "Abierto" in estado_obtenido, f"El estado esperado era 'En proceso', pero se obtuvo: {estado_obtenido}"
