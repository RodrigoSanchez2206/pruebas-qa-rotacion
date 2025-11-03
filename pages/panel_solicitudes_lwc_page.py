import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PanelSolicitudesLWC:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_panel_solicitudes(self):
        nav_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show Navigation Menu']")))
        nav_button.click()

        solicitudes_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/lightning/n/Panel_de_Solicitudes_de_Servicio']")))
        solicitudes_link.click() 

    def wait_for_component_to_load(self):
        # Espera a que el componente esté visible en pantalla
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='truncate title']")))

    def get_lista_estados(self):
        # Espera a que todos los elementos <p> con clase 'slds-text-body_regular' estén presentes
        p_tags = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//p[@class='slds-text-body_regular']")))

        estados = []
        for p in p_tags:
            text = p.text.strip()
            if text.startswith("Estado:"):
                estado = text.replace("Estado:", "").strip()
                estados.append(estado)

        return estados
    
    def get_nombre_tecnico(self):
        # Espera a que todos los elementos <p> con clase 'slds-text-body_regular' estén presentes
        p_tags = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//p[@class='slds-text-body_regular']")))
        nombres_tecnicos = []
        for p in p_tags:
            text = p.text.strip()
            if text.startswith("Técnico:"):
                nombre_tecnico = text.replace("Técnico:", "").strip()
                nombres_tecnicos.append(nombre_tecnico)

        return nombres_tecnicos
    
    def get_disponibilidad(self):
        p_tags = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//p[@class='slds-text-color_success']")))
        disponibilidades = []

        for p in p_tags:
            text = p.text.strip()
            # Dividir por líneas y buscar la línea que contiene "Disponibilidad:"
            for line in text.splitlines():
                if "Disponibilidad:" in line:
                    disponibilidad = line.replace("Disponibilidad:", "").strip()
                    disponibilidades.append(disponibilidad)

        return disponibilidades

    def get_estado(self, nombre_solicitud):
        tarjetas = self.wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//div[contains(@class, 'slds-box_x-small')]"
        )))

        for tarjeta in tarjetas:
            try:
                # Obtener el título de la solicitud
                titulo = tarjeta.find_element(By.XPATH, ".//p[@class='slds-text-heading_small']").text.strip()

                # Si el título coincide con el nombre de la solicitud, proceder con el cambio
                if titulo == nombre_solicitud:
                    # Obtener el texto del estado y eliminar "Estado: "
                    estado = tarjeta.find_element(By.XPATH, ".//p[@class='slds-text-body_regular']").text.strip()
                    estado = estado.replace("Estado: ", "")  # Eliminar "Estado: " para dejar solo el estado
                    return estado  # Retornar solo el estado limpio

            except Exception as e:
                print(f"Error: {e}")
                continue

        return "No existe la solicitud"



    def cambiar_estado(self, nombre_solicitud, nuevo_estado):
        # Esperar a que todas las tarjetas estén presentes
        tarjetas = self.wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//div[contains(@class, 'slds-box_x-small')]"
        )))

        # Buscar la tarjeta que contiene la solicitud con el nombre especificado
        for tarjeta in tarjetas:
            try:
                # Obtener el título de la solicitud
                titulo = tarjeta.find_element(By.XPATH, ".//p[@class='slds-text-heading_small']").text.strip()

                # Si el título coincide con el nombre de la solicitud, proceder con el cambio
                if titulo == nombre_solicitud:
                    # Buscar el combobox para cambiar el estado
                    combobox = tarjeta.find_element(By.XPATH, ".//lightning-combobox//button")
                    combobox.click()  # Abrir el combobox

                    # Esperar a que las opciones estén visibles
                    opciones = self.wait.until(EC.presence_of_all_elements_located((
                        By.XPATH, "//lightning-base-combobox-item[@role='option']"
                    )))

                    # Verificar si la opción está presente y hacer clic
                    for opcion in opciones:
                        opcion_texto = opcion.text.strip()  # Obtener el texto de la opción
                        print(f"Buscando la opción: {opcion_texto}")
                        if opcion_texto == nuevo_estado:
                            opcion.click()  # Hacer clic en la opción correcta
                            print(f"Opción '{nuevo_estado}' seleccionada.")
                            break
                    # Verificar que el estado se haya actualizado correctamente
                    time.sleep(6)
                    estado_actual = self.get_estado(nombre_solicitud)  # Estado ya limpio de "Estado: "
                    return estado_actual.lower() == nuevo_estado.lower()  # Retorna True si el estado es correcto
            except Exception as e:
                print(f"Error: {e}")
                continue
        return False  # Si no se encontró la solicitud o hubo algún error, retornamos False