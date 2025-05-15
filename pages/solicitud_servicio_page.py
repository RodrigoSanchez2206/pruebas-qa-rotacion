# pages/solicitud_servicio_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class SolicitudServicioPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def abrir_modulo_solicitudes(self):
        nav_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show Navigation Menu']")))
        nav_button.click()

        solicitudes_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/lightning/o/Solicitud_de_Servicio__c/home']")))
        solicitudes_link.click()

    def abrir_formulario_nuevo(self):
        nuevo_boton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='New']")))
        nuevo_boton.click()

    def llenar_formulario(self, nombre, contacto, request_type, state, priority, descripcion):

        # Nombre de la solicitud
        campo_nombre = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='Name']")))
        campo_nombre.send_keys(nombre)

        # Hacer clic primero en el campo de búsqueda de contacto
        campo_contacto = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search Contacts...']")))
        campo_contacto.click()
        campo_contacto.clear()
        campo_contacto.send_keys(contacto)

        # Esperar el resultado del dropdown y hacer clic
        contacto_resultado = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//lightning-base-combobox-formatted-text[@title='{contacto}']")))
        contacto_resultado.click()

        # Espera que el campo haya capturado el contacto en su valor visible
        self.wait.until(lambda driver: contacto in driver.page_source)

        # Seleccionar la opción del picklist
        self.seleccionar_opcion_picklist("Request Type", request_type)

        # Selecciionar el estado
        self.seleccionar_opcion_picklist("State", state)

        # Seleccionar la prioridad
        self.seleccionar_opcion_picklist("Priority", priority)

        # Descripción
        descripcion_area = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//textarea[@class='slds-textarea' and @maxlength='255']")
        ))
        descripcion_area.clear()
        descripcion_area.send_keys(descripcion)


        
    def guardar_formulario(self):
        boton_guardar = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[@name='SaveEdit']"))
        )
        boton_guardar.click()
        

    def obtener_errores_en_dialogo(self):
        try:
            # Espera a que aparezca el contenedor de errores globales
            error_dialog = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.slds-popover_error"))
            )

            # Encuentra los <li> dentro de la lista de errores
            errores = error_dialog.find_elements(By.CSS_SELECTOR, "ul.errorsList li")
            return [e.text.strip() for e in errores]

        except Exception as e:
            print(f"No se pudo obtener el diálogo de errores: {e}")
            return []
        
    def seleccionar_opcion_picklist(self, picklist, seleccion):
        try:
            # 1. Esperar que el botón del picklist sea visible y clickeable
            boton_picklist = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//button[@aria-label='{picklist}']"))
            )
            print(f"[DEBUG] Se encontró el botón del picklist: '{boton_picklist.text}'")

            # 2. Scroll hacia el botón y abrir con JS (más confiable)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", boton_picklist)
            self.driver.execute_script("arguments[0].click();", boton_picklist)

            # 3. Esperar a que el menú esté presente
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'slds-listbox')]"))
            )
            time.sleep(0.3)  # Pequeño delay extra

            # 4. Buscar todas las opciones que coincidan
            opciones = self.driver.find_elements(By.XPATH, f"//span[@title='{seleccion}']")
            print(f"[DEBUG] Opciones encontradas con título '{seleccion}': {[o.text for o in opciones]}")

            opcion = None
            for o in opciones:
                if o.is_displayed() and o.is_enabled():
                    opcion = o
                    break

            if not opcion:
                raise TimeoutException(f"No se encontró una opción visible y habilitada con el texto '{seleccion}'")

            # 5. Scroll hacia la opción y clic con JavaScript para mayor fiabilidad
            self.driver.execute_script("arguments[0].scrollIntoView(true);", opcion)
            self.driver.execute_script("arguments[0].click();", opcion)

            print(f"✅ Se seleccionó la opción '{seleccion}'")

            # 6. Confirmar que el valor seleccionado aparece en el botón
            self.esperar_actualizacion_valor_picklist(picklist, seleccion)

        except TimeoutException as e:
            self.driver.save_screenshot(f"error_picklist_{seleccion}.png")
            print(f"[ERROR] No se pudo seleccionar '{seleccion}' en el picklist '{picklist}': {e}")
            raise


    def esperar_actualizacion_valor_picklist(self, picklist, valor_esperado, timeout=20):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                texto_actual = self.driver.find_element(
                    By.XPATH, f"//button[@aria-label='{picklist}']//span[@class='slds-truncate']"
                ).text.strip()
                print(f"[DEBUG] Valor actual del picklist '{picklist}': '{texto_actual}'")
                if texto_actual == valor_esperado:
                    return True
            except Exception as e:
                print(f"[DEBUG] Error al obtener texto del picklist: {e}")
            time.sleep(0.5)
        raise TimeoutException(f"No se actualizó el valor del picklist '{picklist}' a '{valor_esperado}' dentro del tiempo límite.")


    def esperar_formulario_listo(self, picklist):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//button[@aria-label='{picklist}']")
        ))
        time.sleep(0.5)  # Pequeña espera adicional para asegurar que todo está renderizado

    def esperar_redireccion_a_detalle(self, nombre_solicitud):
        xpath = f"//record_flexipage-record-field//lightning-formatted-text[normalize-space(text())='{nombre_solicitud}']"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))


    def verificar_enlace_por_texto(self, texto_visible):
        """
        Verifica si existe un enlace con el texto visible especificado y si está visible.
        Lanza una excepción si el enlace no es visible.
        """
        try:
            elemento = self.driver.find_element(By.LINK_TEXT, texto_visible)
            if not elemento.is_displayed():
                raise Exception(f"❌ El enlace con el texto '{texto_visible}' no está visible.")
        except Exception as e:
            raise Exception(f"⚠️ Error al verificar el enlace: {e}")