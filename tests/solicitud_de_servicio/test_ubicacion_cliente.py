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
        assert latitud.is_displayed(), "El campo de latitud no está visible en el formulario1223."
        assert longitud.is_displayed(), "El campo de longitud no está visible en el formulario12312."

    
    def test_validar_ubicacion_cliente(self):
        solicitud_page = SolicitudServicioPage(self.driver)
        
        solicitud_page.abrir_modulo_solicitudes()
        solicitud_page.abrir_formulario_nuevo()

        solicitud_page.llenar_formulario_con_ubicacion(
            nombre="Solicitud de Servicio con Ubicación",
            contacto="Rodrigo Sanchez",
            request_type="Instalacion",
            state="Abierto",
            priority="Alta",
            descripcion="Descripción para la solicitud con ubicación",
            calle="perlitas",
            numero=7,
            colonia="Barrio norte",
            pais="Mexico",
            codigo_postal="01180",
            ciudad="Ciudad de Mexico",
        )

        solicitud_page.guardar_formulario()
        time.sleep(2)
        self.driver.refresh()
        ubicacion = solicitud_page.obtener_valor_ubicacion()
        assert ubicacion is not None and "," in ubicacion, "No se pudo obtener la ubicación del cliente"
        print(f"Ubicación obtenida: {ubicacion}")
