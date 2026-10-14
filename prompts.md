# Registro de Prompts y Uso de Inteligencia Artificial (PROMPTS.md)

**Proyecto:** Auditor de Permisos de Archivos  
**Asignatura:** Programación I — Tecnicatura Superior en Desarrollo de Software  
**Institución:** IES 9-008 "Manuel Belgrano"  
**Estudiante:** Facundo Julián Saenz  
**Ciclo Lectivo:** 2026  

---

## 📋 Resumen del Uso de la IA

En cumplimiento con las directivas pedagógicas de la cátedra respecto al desarrollo asistido por Inteligencia Artificial ("Vibecoding"), este documento registra la interacción con el modelo de lenguaje **Gemini** utilizado durante el desarrollo del proyecto.

La IA fue empleada bajo el rol de **Tutor Pedagógico y Senior Code Reviewer**, priorizando explicaciones conceptuales, guía paso a paso y depuración asistida para asegurar la comprensión de la lógica del código sin incurrir en copia directa de soluciones no comprendidas.

---

## 💬 Registro de Prompts y Evolución del Proyecto

### Sesión 1: Arquitectura y Diseño Modular

* **Prompt / Consulta del usuario:**
  > "Necesito desarrollar un proyecto integrador en Python llamado 'Auditor de Permisos de Archivos'. Debe seguir una estructura modular estricta de 4 archivos (`main.py`, `estructuras.py`, `persistencia.py`, `utils.py`), sin programación orientada a objetos (usando programación estructurada y diccionarios), nomenclatura `snake_case`, captura de excepciones y algoritmo de ordenamiento burbuja. ¿Cómo planteamos la arquitectura?"
* **Respuesta / Asistencia de la IA:**
  * Explicación de la separación de responsabilidades entre los 4 módulos.
  * Definición de la estructura de datos principal (lista de diccionarios) para representar los metadatos y el riesgo de cada archivo.
  * Elaboración del flujo de trabajo paso a paso.

---

### Sesión 2: Módulo `estructuras.py` y `persistencia.py`

* **Prompt / Consulta del usuario:**
  > "En el archivo persistencia, ¿qué archivos estamos tratando? ¿Los JSON que tienen los datos que definimos en estructuras o los datos de los archivos a analizar?"
* **Respuesta / Asistencia de la IA:**
  * Aclaración conceptual entre los archivos del sistema auditado (que solo se leen) y los archivos del programa (`estado_auditoria.json`, `reporte_riesgos.csv`, `auditoria.log`).
  * Tutoría guiada para la construcción de la función `guardar_datos_json`, identificando el uso de `with open()`, el modo de apertura `'w'` y el manejo de la excepción `IOError`.
  * Explicación de la librería `csv` y el funcionamiento de `csv.DictWriter`, `writeheader()` y `writerows()`.

---

### Sesión 3: Módulo `utils.py` y Algoritmos Core

* **Prompt / Consulta del usuario:**
  > "¿Me podés explicar mejor la lógica de la burbuja?"
* **Respuesta / Asistencia de la IA:**
  * Explicación analógica y técnica del algoritmo Bubble Sort para listas de diccionarios.
  * Análisis del bucle externo `for i in range(n)` y el bucle interno `for j in range(0, n - i - 1)`.
  * Demostración del mecanismo de intercambio (*swap*) sintáctico de Python.
  * Implementación de la función `escanear_directorio` utilizando el módulo nativo `os` y `os.path`.

---

### Sesión 4: Módulo `main.py` y Depuración de Errores

* **Prompt / Consulta del usuario:**
  > "Lo estoy probando, y cuando pongo una opción válida en el menú principal lo toma como si fuera inválida"  
  > *"TypeError: 'NoneType' object is not subscriptable"*  
  > *"AttributeError: 'NoneType' object has no attribute 'keys'"*
* **Respuesta / Asistencia de la IA:**
  * Diagnóstico de la condición lógica en `validar_entero` dentro de `utils.py`.
  * Identificación de valores `None` persistidos en el archivo JSON producto de retornos faltantes en versiones previas de `estructuras.py`.
  * Refactorización y depuración integral de los 4 archivos para asegurar el filtrado de valores nulos, el correcto codificado `utf-8` y la alineación de nombres entre módulos (`exportar_csv`).


---

## 🎯 Conclusiones del Aprendizaje

El uso de la IA en este proyecto permitió:
1. Comprender a fondo el funcionamiento de la persistencia de datos estructurados en formatos JSON y CSV en Python.
2. Afianzar el manejo de excepciones de lectura/escritura (`IOError`, `FileNotFoundError`, `ValueError`).
3. Dominar la abstracción modular dividiendo la lógica de interfaz (`main.py`), procesamiento (`utils.py`), almacenamiento (`persistencia.py`) y datos (`estructuras.py`).
