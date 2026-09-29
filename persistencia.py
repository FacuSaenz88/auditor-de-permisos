import json
import csv
import datetime

def cargar_datos_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except IOError:
        return []

def guardar_datos_json(datos, ruta_archivo):
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)
    except IOError:
        print("[!] Error al escribir datos")

def exportar_csv(datos, ruta_archivo):
    try:
        # 1. Filtramos elementos None o no válidos de la lista
        datos_validos = [d for d in datos if d is not None and isinstance(d, dict)]
        
        if not datos_validos:
            print("[!] No hay datos válidos para exportar.")
            return

        # 2. Obtenemos las claves del primer diccionario válido
        campos = datos_validos[0].keys()
        
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(datos_validos)
            
    except IOError:
        print("[!] Error al intentar exportar el archivo CSV.")

def mostrar_logs(accion, ruta_archivo="auditoria.log"):
    """
    Registra una acción en el archivo de texto log con fecha y hora.
    """
    try:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(ruta_archivo, 'a', encoding='utf-8') as f:
            f.write(f"[{fecha_hora}] - {accion}\n")
    except IOError:
        pass
