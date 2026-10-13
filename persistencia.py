"""
Módulo de Persistencia de Datos.
Encargado de la lectura y escritura de archivos JSON (estado principal),
CSV (reporte para hojas de cálculo) y TXT (log continuo de auditoría).
"""

import json
import csv
import datetime

def cargar_datos_json(ruta_archivo):
    """
    Lee y deserializa el estado guardado en un archivo JSON.
    
    Parámetros:
        ruta_archivo (str): Ruta del archivo JSON a cargar.
        
    Retorna:
        list: Lista de diccionarios cargada desde el archivo o lista vacía si falla.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except IOError:
        return []

def guardar_datos_json(datos, ruta_archivo):
    """
    Serializa y guarda la lista de diccionarios en un archivo JSON con formato legible.
    
    Parámetros:
        datos (list): Lista de diccionarios a guardar.
        ruta_archivo (str): Ruta del archivo de destino.
    """
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            # Serializa la estructura a JSON con indentación de 4 espacios
            json.dump(datos, f, indent=4)
    except IOError:
        print("[!] Error al escribir datos en el archivo JSON.")

def exportar_csv(datos, ruta_archivo):
    """
    Exporta la lista de registros estructurados a un archivo en formato CSV.
    
    Parámetros:
        datos (list): Lista de diccionarios a exportar.
        ruta_archivo (str): Ruta del archivo CSV a generar.
    """
    try:
        # 1. Filtra elementos None o no válidos para evitar errores de atributos
        datos_validos = [d for d in datos if d is not None and isinstance(d, dict)]
        
        if not datos_validos:
            print("[!] No hay datos válidos para exportar.")
            return

        # 2. Extrae las claves del primer diccionario para los encabezados
        campos = datos_validos[0].keys()
        
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()  # Escribe la fila de títulos
            escritor.writerows(datos_validos)  # Escribe todas las filas de datos
            
    except IOError:
        print("[!] Error al intentar exportar el archivo CSV.")

def mostrar_logs(accion, ruta_archivo="auditoria.log"):
    """
    Registra una acción en el archivo de texto plano (log) con marca de tiempo.
    
    Parámetros:
        accion (str): Descripción del evento a registrar.
        ruta_archivo (str): Ruta del archivo .log (por defecto 'auditoria.log').
    """
    try:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(ruta_archivo, 'a', encoding='utf-8') as f:
            f.write(f"[{fecha_hora}] - {accion}\n")
    except IOError:
        pass
