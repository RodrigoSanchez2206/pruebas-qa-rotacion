import time
from tests.base_test import BaseTest
from selenium.webdriver.common.by import By
from pages.panel_solicitudes_lwc_page import PanelSolicitudesLWC
from pages.solicitud_servicio_page import SolicitudServicioPage


class TestValidarSolcitudesActivas(BaseTest):


    def test_cambiar_estado(self):
        nombre_solicitud = "Solicitud Reparacion"  # Cambiar a la solicitud de tu preferencia
        nuevo_estado = "En Proceso"  # El nuevo estado que quieres seleccionar
        
        panel_page = PanelSolicitudesLWC(self.driver)
        panel_page.abrir_panel_solicitudes()
        panel_page.wait_for_component_to_load()
        
        # Cambiar el estado de la solicitud
        cambio_exitoso = panel_page.cambiar_estado(nombre_solicitud, nuevo_estado)
        
        # Verificar que el cambio haya sido exitoso
        assert cambio_exitoso, f"Se esperaba que el estado fuera '{nuevo_estado}', pero no se actualizó correctamente"



        