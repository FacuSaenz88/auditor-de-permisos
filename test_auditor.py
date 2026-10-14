import os
import estructuras
import persistencia
import utils

""" 1. PRUEBAS DE LÓGICA DE DOMINIO (Mínimo 2 exigidas) """

def test_determinar_riesgo():
    """Prueba que la clasificación de riesgo octal sea correcta."""
    assert estructuras.determinar_riesgo('777') == "[!] Alto"
    assert estructuras.determinar_riesgo('666') == "[!] Medio"
    assert estructuras.determinar_riesgo('755') == "[*] Bajo"

def test_generar_estadisticas():
    """Prueba que el cálculo de porcentajes y totales funcione bien."""
    lista_mock = [
        {"riesgo": "[!] Alto"},
        {"riesgo": "[*] Bajo"},
        {"riesgo": "[!] Alto"},
        {"riesgo": "[!] Medio"}
    ]
    total, porcentaje = utils.generar_estadisticas(lista_mock)
    assert total == 4
    assert porcentaje == 50.0  # 2 de 4 archivos son de Alto riesgo

""" 2. PRUEBAS DE PERSISTENCIA (Mínimo 2 exigidas) """

def test_persistencia_json_guardar_y_cargar():
    """Prueba que se pueda guardar un archivo JSON y leer su contenido."""
    archivo_test = "test_datos_temporales.json"
    datos_mock = [{"id": 1, "nombre": "test.txt", "permisos": "777"}]
    
    try:
        persistencia.guardar_datos_json(datos_mock, archivo_test)
        assert os.path.exists(archivo_test)
        
        datos_cargados = persistencia.cargar_datos_json(archivo_test)
        assert len(datos_cargados) == 1
        assert datos_cargados[0]['nombre'] == "test.txt"
    finally:
        # Limpieza del archivo temporal generado
        if os.path.exists(archivo_test):
            os.remove(archivo_test)

def test_cargar_json_inexistente():
    """Prueba que el programa retorne lista vacía si el JSON no existe."""
    datos = persistencia.cargar_datos_json("archivo_inexistente_de_prueba.json")
    assert datos == []

""" 3. PRUEBA DE VALIDACIÓN Y ALGORITMOS (Mínimo 1 exigida) """

def test_ordenar_burbuja_y_filtrar_nulos():
    """Prueba que la burbuja ordene de menor a mayor permiso y limpie valores None."""
    lista_desordenada = [
        {"id": 1, "permisos": "777"},
        None,  # Simulación de registro nulo
        {"id": 2, "permisos": "644"},
        {"id": 3, "permisos": "755"}
    ]
    lista_ordenada = utils.ordenar_por_permisos_burbuja(lista_desordenada)
    
    assert len(lista_ordenada) == 3
    assert lista_ordenada[0]['permisos'] == "644"
    assert lista_ordenada[-1]['permisos'] == "777"
