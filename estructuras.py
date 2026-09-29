import os

def crear_archivo(id_archivo, nombre, ruta, permisos, extension, riesgo):
    """
    Crea y retorna un diccionario representando un archivo escaneado.
    """
    return {
        "id": id_archivo,
        "nombre": nombre,
        "ruta": ruta,
        "extension": extension,
        "permisos": permisos,
        "riesgo": riesgo
    }

def determinar_riesgo(permisos_octal):
    """
    Evalúa los permisos en formato octal y determina el nivel de riesgo.
    """
    permisos_str = str(permisos_octal)
    if permisos_str.endswith('7'):
        return "[!] Alto"
    elif permisos_str.endswith('6'):
        return "[!] Medio"
    else:
        return "[*] Bajo"

def obtener_extension(nombre_archivo):
    """
    Extrae la extensión de un archivo utilizando el módulo os.path.
    """
    _, ext = os.path.splitext(nombre_archivo)
    if ext:
        return ext[1:].lower()
    return "[!] Sin extension"
