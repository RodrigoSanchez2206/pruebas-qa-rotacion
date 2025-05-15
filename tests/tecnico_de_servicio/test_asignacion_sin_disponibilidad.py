import time
from tests.base_test import BaseTest
from pages.solicitud_servicio_page import SolicitudServicioPage
from selenium.webdriver.common.by import By
from pages.tecnicos_de_servicio_page import TecnicosDeServicioPage

class TestAsignacionSinDisponibilidad(BaseTest):

    def test_sin_diponibilidad_consulta(self):
        # Se inicia la page
        solicitud_page = SolicitudServicioPage(self.driver)

        solicitud_page.abrir_modulo_solicitudes()
        solicitud_page.abrir_formulario_nuevo()
        solicitud_page.llenar_formulario(
            nombre="Prueba sin disponibilidad",
            contacto="Rodrigo Sanchez",
            request_type="Consulta",
            state="Abierto",
            priority="Alta",
            descripcion="prueba"
        )
        solicitud_page.guardar_formulario()
        errores = solicitud_page.obtener_errores_en_dialogo()

        campos_esperados = [
            "De momento, no hay técnicos disponibles para esta especialidad: Consulta",
        ]

        for campo in campos_esperados:
            self.assertIn(campo, errores, f"Campo obligatorio no reportado: {campo}")

    def test_sin_diponibilidad_instalacion(self):
        # Se inicia la page
        solicitud_page = SolicitudServicioPage(self.driver)

        solicitud_page.abrir_modulo_solicitudes()
        solicitud_page.abrir_formulario_nuevo()
        solicitud_page.llenar_formulario(
            nombre="Prueba sin disponibilidad",
            contacto="Rodrigo Sanchez",
            request_type="Instalacion",
            state="Abierto",
            priority="Alta",
            descripcion="prueba"
        )
        solicitud_page.guardar_formulario()
        errores = solicitud_page.obtener_errores_en_dialogo()

        campos_esperados = [
            "De momento, no hay técnicos disponibles para esta especialidad: Instalacion",
        ]

        for campo in campos_esperados:
            self.assertIn(campo, errores, f"Campo obligatorio no reportado: {campo}")

    def test_sin_diponibilidad_consulta(self):
        # Se inicia la page
        solicitud_page = SolicitudServicioPage(self.driver)

        solicitud_page.abrir_modulo_solicitudes()
        solicitud_page.abrir_formulario_nuevo()
        solicitud_page.llenar_formulario(
            nombre="Prueba sin disponibilidad",
            contacto="Rodrigo Sanchez",
            request_type="Consulta",
            state="Abierto",
            priority="Alta",
            descripcion="prueba"
        )
        solicitud_page.guardar_formulario()
        errores = solicitud_page.obtener_errores_en_dialogo()

        campos_esperados = [
            "De momento, no hay técnicos disponibles para esta especialidad: Consulta",
        ]

        for campo in campos_esperados:
            self.assertIn(campo, errores, f"Campo obligatorio no reportado: {campo}")

    def sin_diponibilidad_reparacion(self):
        # Se inicia la page
        solicitud_page = SolicitudServicioPage(self.driver)

        solicitud_page.abrir_modulo_solicitudes()
        solicitud_page.abrir_formulario_nuevo()
        solicitud_page.llenar_formulario(
            nombre="Prueba sin disponibilidad",
            contacto="Rodrigo Sanchez",
            request_type="Instalacion",
            state="Abierto",
            priority="Alta",
            descripcion="prueba"
        )
        solicitud_page.guardar_formulario()
        errores = solicitud_page.obtener_errores_en_dialogo()

        campos_esperados = [
            "De momento, no hay técnicos disponibles para esta especialidad: Reparacion",
        ]

        for campo in campos_esperados:
            self.assertIn(campo, errores, f"Campo obligatorio no reportado: {campo}")
    