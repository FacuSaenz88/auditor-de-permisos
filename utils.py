import os
import estructuras

def validar_entero(mensaje, min_val, max_val):
    while True:
        try: 
            valor = int(input(mensaje))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"[!] Error: El número debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("[!] Ingrese un número entero válido.")

def escanear_directorio(ruta_directorio, id_inicial):
    """
    Escanea un directorio usando os y os.path, retornando una lista de diccionarios.
    """
    resultados = []
    
    if not os.path.exists(ruta_directorio):
        print("[!] La ruta especificada no existe.")
        return resultados

    for nombre in os.listdir(ruta_directorio):
        ruta_completa = os.path.join(ruta_directorio, nombre)
        
        if os.path.isfile(ruta_completa):
            estado = os.stat(ruta_completa)
            # Garantiza la extracción exacta de los 3 dígitos octales
            permisos = oct(estado.st_mode & 0o777)[-3:]
            ext = estructuras.obtener_extension(nombre)
            riesgo = estructuras.determinar_riesgo(permisos)
            
            nuevo_registro = estructuras.crear_archivo(id_inicial, nombre, ruta_completa, permisos, ext, riesgo)
            resultados.append(nuevo_registro)
            id_inicial += 1
            
    return resultados

def ordenar_por_permisos_burbuja(lista_archivos):
    """
    Ordena una lista de diccionarios por el campo 'permisos' usando el algoritmo de burbuja.
    Filtra elementos None antes de ordenar.
    """
    lista_limpia = [arch for arch in lista_archivos if arch is not None]
    
    n = len(lista_limpia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_limpia[j]['permisos'] > lista_limpia[j + 1]['permisos']:
                lista_limpia[j], lista_limpia[j + 1] = lista_limpia[j + 1], lista_limpia[j]
                
    return lista_limpia

def generar_estadisticas(lista_archivos):
    """
    Calcula el total de archivos y el porcentaje de archivos con riesgo Alto.
    """
    total = len(lista_archivos)
    
    if total == 0:
        return 0, 0.0
    
    cant_alto_riesgo = 0
    for archivo in lista_archivos:
        if archivo and archivo.get('riesgo') == "[!] Alto":
            cant_alto_riesgo += 1
    
    porcentaje = (cant_alto_riesgo / total) * 100
    return total, porcentaje
