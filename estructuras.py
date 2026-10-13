"""
Módulo de Estructuras de Datos.
Encargado de la definición, construcción y clasificación de registros de archivos,
así como de la generación de firmas de integridad hash y cálculo de riesgos.
"""

import os
import hashlib

def crear_archivo(id_archivo, nombre, ruta, permisos, extension, riesgo):
    """
    Crea y retorna un diccionario estructurado representando un archivo escaneado.
    
    Parámetros:
        id_archivo (int): Identificador único secuencial del registro.
        nombre (str): Nombre del archivo con su extensión.
        ruta (str): Ruta absoluta o relativa completa en el sistema de archivos.
        permisos (str): Permisos en formato octal de 3 dígitos (ej: '777', '644').
        extension (str): Extensión del archivo en minúsculas sin punto.
        riesgo (str): Clasificación calculada del nivel de riesgo.
        
    Retorna:
        dict: Diccionario estructurado con la información del archivo escaneado.
    """
    # Genera un hash SHA-256 único a partir de la ruta para validar integridad
    firma_segura = hashlib.sha256(ruta.encode('utf-8')).hexdigest()
    
    return {
        "id": id_archivo,
        "nombre": nombre,
        "ruta": ruta,
        "extension": extension,
        "permisos": permisos,
        "riesgo": riesgo,
        "firma_hash": firma_segura
    }

def determinar_riesgo(permisos_octal):
    """
    Evalúa los permisos en formato octal y determina el nivel de riesgo de seguridad.
    
    Parámetros:
        permisos_octal (str): Cadena de 3 dígitos octales representando los permisos.
        
    Retorna:
        str: Etiqueta del nivel de riesgo ('[!] Alto', '[!] Medio' o '[*] Bajo').
    """
    permisos_str = str(permisos_octal)
    
    # Evalúa si los permisos de "Otros" incluyen ejecución (7) o lectura/escritura (6)
    if permisos_str.endswith('7'):
        return "[!] Alto"
    elif permisos_str.endswith('6'):
        return "[!] Medio"
    else:
        return "[*] Bajo"

def obtener_extension(nombre_archivo):
    """
    Extrae la extensión de un archivo utilizando el módulo nativo os.path.
    
    Parámetros:
        nombre_archivo (str): Nombre o ruta del archivo a inspeccionar.
        
    Retorna:
        str: Extensión en minúsculas sin el punto inicial, o '[!] Sin extension'.
    """
    _, ext = os.path.splitext(nombre_archivo)
    if ext:
        # Remueve el punto inicial (slicing [1:]) y convierte a minúsculas
        return ext[1:].lower()
    return "[!] Sin extension"
