# pages/tecnicos.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class creacionTecnicos:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def abrir_modulo_tecnicos(self):
        nav_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show Navigation Menu']")))
        nav_button.click()

        solicitudes_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/lightning/o/Tecnico_de_Servicio__c/home']")))
        solicitudes_link.click()

    def abrir_formulario_nuevo(self):
        nuevo_boton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='New']")))
        nuevo_boton.click()

    def llenar_formulario(self, nombre, apellido, request_type):
        try:
            # Llenar campos de texto
            nombre_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Nombre__c']")))
            nombre_input.send_keys(nombre)

            apellido_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Apellido__c']")))
            apellido_input.send_keys(apellido)

            # Seleccionar opción en el picklist de "Request Type"
            self.seleccionar_opcion_picklist("Especialidad", request_type)

        except Exception as e:
            print(f"❌ No se pudo llenar el formulario: {e}")

        
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


    def guardar_formulario(self):
        boton_guardar = self.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[@name='SaveEdit']")))
        boton_guardar.click()
        
    def volver_a_lista_tecnicos(self):
        nav_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show Navigation Menu']")))
        nav_button.click()

        solicitudes_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/lightning/o/Tecnico_de_Servicio__c/home']")))
        solicitudes_link.click()
        nuevo_boton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='New']")))
        nuevo_boton.click()
    
    def validar_opciones_picklist_seleccionables(self, picklist, valores_esperados):
        for valor in valores_esperados:
            try:
                boton_picklist = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, f"//button[@aria-label='{picklist}']"))
                )
                self.driver.execute_script("arguments[0].scrollIntoView(true);", boton_picklist)
                self.driver.execute_script("arguments[0].click();", boton_picklist)
                self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'slds-listbox')]"))
                )
                time.sleep(0.3)
                opciones = self.driver.find_elements(By.XPATH, f"//span[@title='{valor}']")
                opcion = next((o for o in opciones if o.is_displayed() and o.is_enabled()), None)
                if not opcion:
                    raise Exception(f"No se encontró la opción visible y seleccionable: '{valor}'")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", opcion)
                self.driver.execute_script("arguments[0].click();", opcion)
                self.esperar_actualizacion_valor_picklist(picklist, valor)
                print(f"✅ Validado: se puede seleccionar la opción '{valor}'")
            except Exception as e:
                raise AssertionError(f"❌ Error al validar la opción '{valor}' del picklist '{picklist}': {e}")
            
    def validar_error_por_campos_vacios(self):
        try:
            # Hacer clic en guardar con campos vacíos
            boton_guardar = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@name='SaveEdit']"))
            )
            boton_guardar.click()

            # Esperar a que aparezca un mensaje de error en campos obligatorios
            mensaje_error = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='window']")))
            print(f"✅ Se detectó mensaje de error de validación: '{mensaje_error.text.strip()}'")
            return True
        except Exception:
            raise AssertionError("❌ No se detectaron errores ni validaciones al guardar el formulario vacío.")
        


    def validar_error_nombre(self, apellido, especialidad):
        try:
            # Dejar el campo Nombre vacío, llenar los otros campos
            apellido_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Apellido__c']")))
            apellido_input.send_keys(apellido)

            self.seleccionar_opcion_picklist("Especialidad", especialidad)

            # Hacer clic en guardar
            boton_guardar = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='SaveEdit']")))
            boton_guardar.click()

            # Esperar que aparezca el mensaje en la lista de errores
            error_en_lista = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-index='0']"))
            )
            mensaje = error_en_lista.text.strip()
            print(f"✅ Se detectó error de validación en la lista de errores: '{mensaje}'")

            # Validar que el mensaje menciona el campo requerido
            assert "nombre" in mensaje.lower() or "required" in mensaje.lower(), \
                f"❌ El mensaje no parece referirse al campo 'Nombre': '{mensaje}'"

        except Exception as e:
            raise AssertionError(f"❌ No se detectó validación para campo 'Nombre' mediante data-index: {e}")
        

    def validar_error_apellido(self, nombre, especialidad):
        try:
            # Dejar el campo Nombre vacío, llenar los otros campos
            nombre_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Nombre__c']")))
            nombre_input.send_keys(nombre)

            self.seleccionar_opcion_picklist("Especialidad", especialidad)

            # Hacer clic en guardar
            boton_guardar = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='SaveEdit']")))
            boton_guardar.click()
            time.sleep(5)
            # Esperar que aparezca el mensaje en la lista de errores
            error_en_lista = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-index='0']"))
            )
            mensaje = error_en_lista.text.strip()
            print(f"✅ Se detectó error de validación en la lista de errores: '{mensaje}'")

            # Validar que el mensaje menciona el campo requerido
            assert "apellido" in mensaje.lower() or "required" in mensaje.lower(), \
                f"❌ El mensaje no parece referirse al campo 'Nombre': '{mensaje}'"

        except Exception as e:
            raise AssertionError(f"❌ No se detectó validación para campo 'Apellido' mediante data-index: {e}")
        

    def validar_error_picklist(self, nombre, apellido, especialidad):
        try:
            # Dejar el campo Nombre vacío, llenar los otros campos
            nombre_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Nombre__c']")))
            nombre_input.send_keys(nombre)
            apellido_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Apellido__c']")))
            apellido_input.send_keys(apellido)

            self.seleccionar_opcion_picklist("Especialidad", especialidad)

            # Hacer clic en guardar
            boton_guardar = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='SaveEdit']")))
            boton_guardar.click()
            # Esperar que aparezca el mensaje en la lista de errores
            error_en_lista = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-index='0']"))
            )
            mensaje = error_en_lista.text.strip()
            print(f"✅ Se detectó error de validación en la lista de errores: '{mensaje}'")

            # Validar que el mensaje menciona el campo requerido
            assert "especialidad" in mensaje.lower() or "required" in mensaje.lower(), \
                f"❌ El mensaje no parece referirse al campo 'Especialidad': '{mensaje}'"

        except Exception as e:
            raise AssertionError(f"❌ No se detectó validación para campo 'Especialidad' mediante data-index: {e}")    