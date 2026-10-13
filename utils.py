"""
Módulo de Utilidades y Herramientas Auxiliares.
Contiene funciones de validación de entrada, escaneo del sistema de archivos,
algoritmos de ordenamiento propio (burbuja) y generación de estadísticas.
"""

import os
import estructuras

def validar_entero(mensaje, min_val, max_val):
    """
    Pide un número entero al usuario y valida que se encuentre en un rango numérico.
    
    Parámetros:
        mensaje (str): Texto a mostrar en el input.
        min_val (int): Valor entero mínimo permitido.
        max_val (int): Valor entero máximo permitido.
        
    Retorna:
        int: El entero válido ingresado por el usuario.
    """
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
    Escanea un directorio del disco duro creando una lista de registros escaneados.
    
    Parámetros:
        ruta_directorio (str): Ruta de la carpeta a inspeccionar.
        id_inicial (int): ID con el que comenzará la numeración secuencial.
        
    Retorna:
        list: Lista de diccionarios con los archivos encontrados y analizados.
    """
    resultados = []
    
    # 1. Verifica si la ruta ingresada existe en el equipo
    if not os.path.exists(ruta_directorio):
        print("[!] La ruta especificada no existe.")
        return resultados

    # 2. Recorre los elementos dentro del directorio
    for nombre in os.listdir(ruta_directorio):
        ruta_completa = os.path.join(ruta_directorio, nombre)
        
        # Filtra para procesar únicamente archivos (omite carpetas)
        if os.path.isfile(ruta_completa):
            estado = os.stat(ruta_completa)
            # Extrae exactamente los últimos 3 dígitos octales usando máscara de bits
            permisos = oct(estado.st_mode & 0o777)[-3:]
            ext = estructuras.obtener_extension(nombre)
            riesgo = estructuras.determinar_riesgo(permisos)
            
            # Construye el objeto de datos llamando al módulo estructuras
            nuevo_registro = estructuras.crear_archivo(id_inicial, nombre, ruta_completa, permisos, ext, riesgo)
            resultados.append(nuevo_registro)
            id_inicial += 1
            
    return resultados

def ordenar_por_permisos_burbuja(lista_archivos):
    """
    Ordena una lista de diccionarios por permisos de menor a mayor usando Bubble Sort.
    
    Parámetros:
        lista_archivos (list): Lista de diccionarios de archivos a ordenar.
        
    Retorna:
        list: Lista ordenada por la clave 'permisos'.
    """
    # Descarta elementos nulos que pudieran existir en la lista
    lista_limpia = [arch for arch in lista_archivos if arch is not None]
    
    n = len(lista_limpia)
    # Algoritmo de Burbuja: compara e intercambia pares contiguos
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_limpia[j]['permisos'] > lista_limpia[j + 1]['permisos']:
                # Intercambio de valores directo (swap de Python)
                lista_limpia[j], lista_limpia[j + 1] = lista_limpia[j + 1], lista_limpia[j]
                
    return lista_limpia

def generar_estadisticas(lista_archivos):
    """
    Calcula el total de archivos escaneados y el porcentaje con riesgo 'Alto'.
    
    Parámetros:
        lista_archivos (list): Lista de diccionarios escaneados.
        
    Retorna:
        tuple: (total_archivos, porcentaje_alto_riesgo)
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
