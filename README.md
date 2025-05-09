# Pruebas Rotación QA

## Tabla de Contenidos

* [Introducción](#introducción)
* [Características Principales](#características-principales)
* [Instalación](#instalación)
* [Uso](#uso)

## Introducción

Este repositorio incluye todas las pruebas automatizadas del proyecto de rotación de QA.

## Características Principales

* Uso de Selenium
* Pruebas de una instancia developer edition de salesforce

## Instalación

1.  **Requisitos Previos:**
    * python >= 3.13.2


2.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/RodrigoSanchez2206/pruebas-qa-rotacion.git
    cd
    ```

3.  **Crear y Activar el Entorno Virtual (Recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En macOS/Linux
    # venv\Scripts\activate  # En Windows
    ```

4.  **Instalar las Dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar tus pruebas, asegúrate de haber activado tu entorno virtual y tener instaladas las dependencias.

### Ejecutar una Prueba Específica

Puedes ejecutar un archivo de prueba directamente usando:

    ```bash
    python -m unittest tests/solicitud_de_servicio/test_validacion_campos_obligatorios.py
    ```
### Ejecutar todos los test 

    ```bash
    python -m unittest discover -s tests/solicitud_de_servicio -p "test_*.py"
    ```
