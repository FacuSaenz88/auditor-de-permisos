import os
import estructuras

def validar_entero(mensaje, min_val, max_val):
    while True:
        try: 
            valor = int(input(mensaje))
            if min_val <= valor <= max_val:
                print("[!] numero incorrecto, ingrese uno valido porfavor")
            else:
                print(f"[!] Error: El número debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("[!] Ingrese un numero entero valido")

def escanear_directorio(ruta_directorio, id_inicial):
    """
    Escanea un directorio usando os y os.path, retornando una lista de diccionarios.
    """
    resultados = []
    
    # 1. Verificamos si la ruta existe con os.path.exists
    if not os.path.exists(ruta_directorio):
        print("[!] La ruta especificada no existe.")
        return resultados

    # 2. Recorremos los elementos del directorio con os.listdir
    for nombre in os.listdir(ruta_directorio):
        # Unimos la carpeta con el nombre del archivo usando os.path.join[cite: 1]
        ruta_completa = os.path.join(ruta_directorio, nombre)
        
        # Verificamos si es un archivo (y no una carpeta)
        if os.path.isfile(ruta_completa):
            # Obtenemos permisos con os.stat
            estado = os.stat(ruta_completa)
            permisos = oct(estado.st_mode)[-3:] # Extraemos los últimos 3 dígitos octales
            ext = estructuras.obtener_extension(nombre)
            riesgo = estructuras.determinar_riesgo(permisos)
            
            nuevo_registro = estructuras.crear_archivo(id_inicial, nombre, ruta_completa, permisos, ext, riesgo)
            resultados.append(nuevo_registro)
            id_inicial += 1
    return resultados

def ordenar_por_permisos_burbuja(lista_archivos):
#Ordena una lista de diccionarios por el campo 'permisos' usando el algoritmo de burbuja.
    n = len(lista_archivos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_archivos[j]['permisos'] > lista_archivos[j + 1]['permisos']:
                # Intercambio (swap) en una sola línea en Python
                lista_archivos[j], lista_archivos[j + 1] = lista_archivos[j + 1], lista_archivos[j]
    return lista_archivos

def generar_estadisticas(lista_archivos):
    #Calcula el total de archivos y el porcentaje de archivos con riesgo Alto.Retorna una tupla: (total, porcentaje_alto_riesgo).
    total = len(lista_archivos)
    
    if total == 0:
        return 0, 0.0
    
    cant_alto_riesgo = 0
    for archivo in lista_archivos:
        if archivo['riesgo'] == "[!] Alto":
            cant_alto_riesgo += 1
    
    porcentaje = (cant_alto_riesgo / total) * 100
    return total, porcentaje