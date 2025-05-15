import time
from tests.base_test import BaseTest
from selenium.webdriver.common.by import By
from pages.panel_solicitudes_lwc_page import PanelSolicitudesLWC
from pages.solicitud_servicio_page import SolicitudServicioPage


class TestValidarVisibilidadCampos(BaseTest):

    def test_validar_nombre_tecnico(self):
        panel_page = PanelSolicitudesLWC(self.driver)
        panel_page.abrir_panel_solicitudes()
        panel_page.wait_for_component_to_load()

        nombres_tecnicos = panel_page.get_nombre_tecnico()
        for nombre_tecnico in nombres_tecnicos:
            print(f"Técnico encontrado: {nombre_tecnico}")
            self.assertNotEqual(nombre_tecnico.lower(), "sin asignar", f"Se encontró una solicitud sin técnico asignado: {nombre_tecnico}")
    
    def test_validar_visibilidad_disponibilidad(self):
        panel_page = PanelSolicitudesLWC(self.driver)
        panel_page.abrir_panel_solicitudes()
        panel_page.wait_for_component_to_load()
        
        disponibilidades = panel_page.get_disponibilidad()
        for disponibilidad in disponibilidades:
            print(f"Disponibilidad encontrada: {disponibilidad}")
            self.assertNotEqual(disponibilidad.lower(), "no disponible", f"Se encontró una solicitud con disponibilidad no válida: {disponibilidad}")
