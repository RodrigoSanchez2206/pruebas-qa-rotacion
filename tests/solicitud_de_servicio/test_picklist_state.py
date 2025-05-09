from tests.base_test import BaseTest
from pages.solicitud_servicio_page import SolicitudServicioPage

class TestPickListPriority(BaseTest):
    
        
    def realizar_seleccion_picklist(self, opcion, picklist):
        # Método común para abrir el formulario, esperar y seleccionar una opción de picklist
        solicitud_page = SolicitudServicioPage(self.driver)
        
        solicitud_page.abrir_modulo_solicitudes()
        solicitud_page.abrir_formulario_nuevo()
        solicitud_page.esperar_formulario_listo(picklist)
        solicitud_page.seleccionar_opcion_picklist(picklist, opcion)

    def test_picklist_alta(self):
        self.realizar_seleccion_picklist("Abierto", "State")
    
    def test_picklist_baja(self):
        self.realizar_seleccion_picklist("En proceso", "State")

    def test_picklist_media(self):
        self.realizar_seleccion_picklist("Cerrado", "State")