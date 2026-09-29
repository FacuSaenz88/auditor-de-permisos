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
        
def exportar_datos(datos, ruta_archivo):
    try:
        with open(ruta_archivo, 'w', newline='') as f:
            if not datos:
                return
            else:
                campos = datos[0].keys()
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(datos)
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