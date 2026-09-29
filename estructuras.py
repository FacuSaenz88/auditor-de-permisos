import os

def crear_archivo(id_archivo, nombre, ruta, permisos, extension, riesgo):
    datos = {
        "id": id_archivo,
        "nombre": nombre,
        "ruta": ruta,
        "extension": extension,
        "permisos": permisos,
        "riesgo": riesgo
    }
    """
    Crea y retorna un diccionario representando un archivo escaneado.
    
    Parámetros:
        id_archivo (int): Identificador único del registro.
        nombre (str): Nombre del archivo con su extensión.
        ruta (str): Ruta completa en el sistema de archivos.
        permisos (str): Permisos en formato octal (ej: '777').
        extension (str): Extensión del archivo en minúsculas.
        riesgo (str): Clasificación del nivel de riesgo.
        
    Retorna:
        dict: Diccionario estructurado con los datos del archivo.
    """
    
def determinar_riesgo(permisos_octal):
    permisos_str = str(permisos_octal)
    if permisos_str.endswith('7'):
        return "[!] Alto"
    elif permisos_str.endswith('6'):
        return "[!] Medio"
    else:
        return "[*] Bajo"
"""
    Evalúa los permisos en formato octal y determina el nivel de riesgo.
    
    Parámetros:
        permisos_octal (str|int): Permisos en formato octal (ej: '755').
        
    Retorna:
        str: Cadena indicando el nivel de riesgo.
"""
        
def obtener_extension(nombre_archivo):
    _, ext = os.path.splitext(nombre_archivo)
    if ext:
        return ext[1:].lower()
    return "[!] Sin extension"

"""
    Extrae la extensión de un archivo utilizando el módulo os.path.
    
    Parámetros:
        nombre_archivo (str): Nombre o ruta del archivo.
        
    Retorna:
        str: Extensión en minúsculas sin el punto, o '[!] Sin extension'.
"""