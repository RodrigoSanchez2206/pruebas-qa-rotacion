from tests.base_test import BaseTest
from pages.solicitud_servicio_page import SolicitudServicioPage

class TestValidacionCamposObligatorios(BaseTest):
    

    def test_validacion_campos_obligatorios(self):
        # Se inicia la page
        solicitud_page = SolicitudServicioPage(self.driver)

        solicitud_page.abrir_modulo_solicitudes()
        solicitud_page.abrir_formulario_nuevo()
        solicitud_page.guardar_formulario()
        errores = solicitud_page.obtener_errores_en_dialogo()

        campos_esperados = [
            "Solicitud de Servicio Name",
            "Request Type",
            "State",
            "Priority",
            "Description",
            "Related client"
        ]

        for campo in campos_esperados:
            self.assertIn(campo, errores, f"Campo obligatorio no reportado: {campo}")

            
    