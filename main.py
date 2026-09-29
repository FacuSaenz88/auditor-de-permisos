import estructuras
import persistencia
import utils

def submenu_consultas(estado_archivos):
    if not estado_archivos:
        print("\[!] No hay archivos registrados. Escanee un directorio primero")
        return
    
    print("\n--- Submenú de Consulta y Filtros ---")
    print("1. Ver todos ordenados por permisos (Menor a Mayor)")
    print("2. Filtrar por nivel de riesgo (Alto / Medio / Bajo)")
    
    opcion = utils.validar_entero("Seleccione una opción (1-2): ", 1, 2)
    
    if opcion == 1:
        # Hacemos una copia para no alterar el orden original y ordenamos con burbuja
        ordenados = utils.ordenar_por_permisos_burbuja(estado_archivos.copy())
        print("\n--- ARCHIVOS ORDENADOS POR PERMISOS ---")
        for arch in ordenados:
            print(f"ID: {arch['id']} | Nombre: {arch['nombre']} | Permisos: {arch['permisos']} | Riesgo: {arch['riesgo']}")
            
    elif opcion == 2:
        riesgo_buscado = input("Ingrese el nivel de riesgo a buscar (Alto/Medio/Bajo): ").strip().capitalize()
        filtrados = [arch for arch in estado_archivos if riesgo_buscado in arch['riesgo']]
        
        if filtrados:
            print(f"\n--- ARCHIVOS CON RIESGO '{riesgo_buscado}' ---")
            for arch in filtrados:
                print(f"ID: {arch['id']} | Nombre: {arch['nombre']} | Permisos: {arch['permisos']} | Ruta: {arch['ruta']}")
        else:
            print(f"\n[!] No se encontraron archivos con el riesgo '{riesgo_buscado}'.")



def menu_principal():
    archivo_json = "estado_auditoria.json"
    estado_archivos = persistencia.cargar_datos_json(archivo_json)
    persistencia.mostrar_logs("[+] Inicio de sesion de la aplicacion")
    while True:
        print("""======= Auditor de Permisos de Archivos =======
                By: Facundo Saenz, Ivo gonzales, 
        ======= Ignacio Montagna y Federico Calafiore ======""")
        print("1. Escanear directorio")
        print("2. Consultar y filtrar archivos (Submenu)")
        print("3. Eliminar registro de archivo")
        print("4. Ver estadisticas de riesgo")
        print("5. Exportar CSV")
        print("6. Salir")
        
        opcion = utils.validar_entero("Seleccione una opcion (1-6): ", 1, 6)
        
        if opcion == 1:
            ruta = input("\n[*] Ingrese la ruta del directorio a escanear (e.j: '.' para la carpeta actual) ")
            id_inicio = len(estado_archivos) + 1
            
            nuevos_archivos = utils.escanear_directorio(ruta, id_inicio)
            if nuevos_archivos:
                estado_archivos.extend(nuevos_archivos)
                persistencia.guardar_datos_json(estado_archivos, archivo_json)
                persistencia.mostrar_logs(f"[+] Escaneo de directorio exitoso!: {ruta}")
                print(f"\n[+] Escaneo finalizado. Se agregaron {len(nuevos_archivos)}")
            else:
                print(f"\n[!] No se agregaron archivos")
        
        elif opcion == 2:
            submenu_consultas(estado_archivos)
            persistencia.mostrar_logs("Consuta realizada en el submenu")
            
        elif opcion == 3:
            if not estado_archivos:
                print("\n[!] No hay ningun registro que eliminar")
                continue
            
            id_eliminar = utils.validar_entero("\n[*] Ingrese el ID del archivo a eliminar del registro", 1, 99999)
            total_antes = len(estado_archivos)
            
            estado_archivos = [arch for arch in estado_archivos if arch['id'] != id_eliminar]
            
            if len(estado_archivos) < total_antes:
                persistencia.guardar_datos_json(estado_archivos, archivo_json)
                persistencia.registrar_log(f"Registro con ID {id_eliminar} eliminado")
                print(f"\n[+] Registro ID {id_eliminar} eliminado correctamente.")
            else:
                print("\n[!] No se encontró ningún archivo con ese ID.")
        
        elif opcion == 4:
            total, porcentaje = utils.generar_estadisticas(estado_archivos)
            print("\n=== ESTADÍSTICAS DE AUDITORÍA ===")
            print(f"Total de archivos escaneados: {total}")
            print(f"Porcentaje con Alto Riesgo: {porcentaje:.2f}%")
            persistencia.registrar_log("Visualización de estadísticas")
            
        elif opcion == 5:
            if not estado_archivos:
                print("\n[!] No hay datos para exportar")
                continue
            
            archivo_csv = "reporte_riesgos.csv"
            persistencia.exportar_csv(estado_archivos, archivo_csv)
            persistencia.registrar_log(f"Reporte exportado a {archivo_csv}")
            print(f"\n[+] Reporte exportado exitosamente como '{archivo_csv}'.")
            
        elif opcion == 6:
            persistencia.guardar_datos_json(estado_archivos, archivo_json)
            persistencia.registrar_log("Cierre de sesión de la aplicación")
            print("\n[*] Guardando estado y cerrando el sistema.")
            break
        
if __name__ == '__main__':
    menu_principal()