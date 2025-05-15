import time
from tests.base_test import BaseTest
from pages.tecnicos import creacionTecnicos
from selenium.webdriver.common.by import By

class creacion_tecnicos(BaseTest):
    def test_crear_solicitudes_para_tipos_y_validar_envio(self):
        tipos = ["Reparacion", "Instalacion", "Consulta"]
        
        for tipo in tipos:
            print(f"\n🔄 Procesando tipo: {tipo}")
            try:
                tecnicos_page = creacionTecnicos(self.driver)
                tecnicos_page.abrir_modulo_tecnicos()
                tecnicos_page.abrir_formulario_nuevo()

                tecnicos_page.llenar_formulario(
                    nombre="Johan",
                    apellido="Garcia",
                    request_type=tipo
                )

                tecnicos_page.guardar_formulario()
                time.sleep(5)
            except Exception as e:
                print(f"❌ Error al procesar tipo '{tipo}': {e}")
