# Automatización de Pruebas con Python
## Propósito del Proyecto

Este proyecto tiene como objetivo automatizar pruebas funcionales de una aplicación web utilizando herramientas de testing en Python.

Se busca validar el correcto funcionamiento de distintas funcionalidades mediante pruebas automatizadas, mejorando la calidad del software y reduciendo el esfuerzo manual.

---

## Tecnologías Utilizadas

- Python → Lenguaje principal de desarrollo  
- Pytest → Framework de testing  
- Selenium WebDriver → Automatización de navegadores  
- pytest-html → Generación de reportes en HTML  

---

## ⚙️ Instalación de Dependencias

### 1. Clonar el repositorio
    git clone https://github.com/ceurrutia/pre-entrega-automation-testing-cecilia-urrutia.git

### 2. Crear entorno virtual (opcional pero recomendado)
    python -m venv env

### 3. Activar entorno virtual

En Windows:
    venv\Scripts\activate

En Linux/Mac:
    source venv/bin/activate

### 4. Instalar dependencias
    pip install -r requirements.txt

---


## Ejecución de Pruebas

Ejecutar las pruebas con:
    pytest tests/test_saucedemo.py -v

---

## Generación de Reportes

Generar reporte HTML con:
    pytest pre-entrega-final/tests/test_saucedemo.py -v --html=reporte.html

El archivo generado será:
    /reports/report.html

Abrirlo en un navegador para ver el detalle de ejecución.

---

## Estructura del Proyecto

    project/

├── conftest.py

├── requirements.txt

├── README.md

├── .gitignore

│
├── tests/\

│   ├── test_saucedemo.py

│   └── commons/

│       ├── __init__.py

│       └── funciones_commons.py
│
├── utils/

├── data/

├── reports/

│   └── report.html
