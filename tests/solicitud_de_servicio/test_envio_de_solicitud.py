import time
from tests.base_test import BaseTest
from pages.solicitud_servicio_page import SolicitudServicioPage
from selenium.webdriver.common.by import By

class TestEnvioDeSolicitud(BaseTest):
    
    def test_crear_solicitudes_para_tipos_y_validar_envio(self):
        solicitud_page = SolicitudServicioPage(self.driver)

        tipos = ["Instalacion", "Reparacion", "Consulta"]

        for tipo in tipos:
            solicitud_page.abrir_modulo_solicitudes()
            solicitud_page.abrir_formulario_nuevo()

            solicitud_page.llenar_formulario(
                nombre=f"Solicitud {tipo}",
                contacto="Rodrigo Sanchez",
                request_type=tipo,
                state="Abierto",
                priority="Alta",
                descripcion=f"Descripción para {tipo}"
            )
            solicitud_page.guardar_formulario()
            solicitud_page.esperar_redireccion_a_detalle(f"Solicitud {tipo}")
