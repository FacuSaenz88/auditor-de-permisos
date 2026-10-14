# Auditor de Permisos de Archivos 🛡️

**Tecnicatura Superior en Desarrollo de Software — Programación I**  
Ciclo Lectivo 2026 — Proyecto Integrador (Segundo Semestre)

---

## 👥 Integrantes del Equipo

* **Facundo Julián Saenz**
* **Ignacio Montagna**
* **Ivo Gonzales**
* **Federico Calafiore**
* **Magalí Badilla**
* **Marilu Casana**

---

## 📝 Descripción del Proyecto

El **Auditor de Permisos de Archivos** es una aplicación de consola desarrollada en Python que permite inspeccionar y auditar directorios del sistema de archivos local. Su objetivo principal es detectar permisos de archivos excesivos o potencialmente inseguros que puedan representar un riesgo de seguridad o exposición de datos no autorizada.

La aplicación permite:

* Escanear directorios locales utilizando las bibliotecas nativas `os` y `os.path`.
* Generar una **firma digital criptográfica (hash SHA-256)** mediante `hashlib` para verificar la integridad y unicidad de cada registro de archivo escaneado.
* Clasificar el nivel de riesgo de cada archivo según sus permisos octales.
* Filtrar y ordenar los hallazgos mediante algoritmos propios (ordenamiento burbuja).
* Generar estadísticas descriptivas sobre el nivel de riesgo y los tipos de archivo.
* Mantener la persistencia del estado en formato JSON, exportar reportes ejecutivos en CSV y registrar un historial de operaciones (log) en un archivo TXT plano.

---

## 🛠️ Tecnologías y Bibliotecas Utilizadas

El proyecto utiliza exclusivamente la **biblioteca estándar de Python 3.10+**, garantizando portabilidad sin necesidad de instalar dependencias externas para la lógica del sistema:

* **`os` / `os.path`**: Inspección del sistema de archivos, consulta de permisos y metadatos (`os.stat`) y construcción portable de rutas (`os.path.join`).
* **`hashlib`**: Generación de hashes criptográficos (SHA-256) para asegurar la integridad de cada archivo en la auditoría.
* **`json`**: Serialización y deserialización del estado principal del programa (`estado_auditoria.json`).
* **`csv`**: Exportación de reportes tabulares estructurados (`reporte_riesgos.csv`).
* **`datetime`**: Generación de marcas de tiempo (*timestamps*) para el registro continuo de operaciones (`auditoria.log`).
* **`pytest` / `unittest`**: Ejecución del conjunto de pruebas unitarias automatizadas.

---

## 📂 Estructura de Archivos del Proyecto

```text
auditor_permisos/
│
├── main.py               # Punto de entrada. Administra el flujo del programa y los menús.
├── estructuras.py        # Modelado de datos (diccionarios), funciones constructoras y generación de hash SHA-256.
├── persistencia.py       # Lectura/escritura de archivos (JSON, CSV y log TXT).
├── utils.py              # Validaciones de entrada, escaneo de directorios, burbuja y estadísticas.
├── test_auditor.py       # Pruebas unitarias automatizadas con pytest.
│
├── README.md             # Documentación general e instrucciones del proyecto.
├── PROMPTS.md            # Registro transparente del uso de IA en el desarrollo.
│
├── estado_auditoria.json # Base de datos principal (generado en la primera ejecución).
├── reporte_riesgos.csv   # Reporte exportable para hojas de cálculo (generado a demanda).
└── auditoria.log         # Historial de acciones con marcas de tiempo (generado continuamente).
