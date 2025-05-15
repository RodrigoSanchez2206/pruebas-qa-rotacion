import time
from tests.base_test import BaseTest
from pages.solicitud_servicio_page import SolicitudServicioPage
from selenium.webdriver.common.by import By
from pages.tecnicos_de_servicio_page import TecnicosDeServicioPage

class TestAsignacionAutomatica(BaseTest):

    def test_asignacion_automatica_reparacion(self):
        solicitud_page = SolicitudServicioPage(self.driver)

        tipos = ["Reparacion"]

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
            solicitud_page.obtener_tecnico_asignado()
            tecnico_page = TecnicosDeServicioPage(self.driver)
            tecnico_page.obtener_especialidad()
            print("✅ Paso el test con ", tipo)

    def test_asignacion_automatica_instalacion(self):
        solicitud_page = SolicitudServicioPage(self.driver)

        tipos = ["Instalacion"]

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
            solicitud_page.obtener_tecnico_asignado()
            tecnico_page = TecnicosDeServicioPage(self.driver)
            tecnico_page.obtener_especialidad()
            print("✅ Paso el test con ", tipo)

    def test_asignacion_automatica_consulta(self):
        solicitud_page = SolicitudServicioPage(self.driver)

        tipos = ["Consulta"]

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
            solicitud_page.obtener_tecnico_asignado()
            tecnico_page = TecnicosDeServicioPage(self.driver)
            tecnico_page.obtener_especialidad()
            print("✅ Paso el test con ", tipo)