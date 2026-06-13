# Módulos del proyecto
from gestion_paises import agregar_pais, actualizar_datos
from consultas import busqueda_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas

# Programa principal
while True:
    print()
    print("\t\t=====-----MENU-----=====")
    opcion = input("""
    1. Agregar país
    2. Actualizar país
    3. Buscar país
    4. Filtrar países
    5. Ordenar países
    6. Estadísticas
    0. Salir
    """)
    try:
        opcion = int(opcion)
        match opcion:
            case 0:
                print("Usted salio del programa")
                break
            case 1:
                agregar_pais()
            case 2:
                actualizar_datos()
            case 3:
                busqueda_pais()
            case 4:
                filtrar_paises()
            case 5:
                ordenar_paises()
            case 6:
                mostrar_estadisticas()
            case _:
                print("Numero fuera de rango")
    except ValueError:
        print("\tIngrese un numero entero")