from tests.base_test import BaseTest
from pages.solicitud_servicio_page import SolicitudServicioPage
import time
from tests.base_test import BaseTest
from pages.solicitud_servicio_page import SolicitudServicioPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestUbicacionCliente(BaseTest):
    
    def test_validar_existencia_campo_ubicacion(self):
        # Método para validar la existencia del campo de ubicación
        solicitud_page = SolicitudServicioPage(self.driver)
        
        # Abrir el módulo de solicitudes
        solicitud_page.abrir_modulo_solicitudes()
        # Abrir el formulario nuevo
        solicitud_page.abrir_formulario_nuevo()
        # Validar que el campo de ubicación esté presente
        latitud = solicitud_page.obtener_latitud()
        longitud = solicitud_page.obtener_longitud()
        assert latitud.is_displayed(), "El campo de latitud no está visible en el formulario."
        assert longitud.is_displayed(), "El campo de longitud no está visible en el formulario."