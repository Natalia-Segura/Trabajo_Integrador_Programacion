# Ordenar países por: Nombre, Población, Superficie (ascendente o descendente)

def ordenar_paises():

#Creo lista vacía para guardar los países
    lista_paises = []

#Abro el archivo CSV
    with open("paises.csv", "r", encoding="utf-8") as archivo:

#Recorro cada línea del archivo
        for linea in archivo:
#Elimino saltos de línea y separo los datos
            datos = linea.strip().split(",")
#Evito errores por filas inválidas
            if len(datos) < 4:
                continue
#Ignoro la fila de encabezado
            if datos[0].lower() == "nombre":
                continue
#Guardo cada país dentro de la lista
            lista_paises.append(datos)

#Menú de opciones
    menu = """
    Elija cómo quiere ordenar los países:

    1. Nombre
    2. Población
    3. Superficie
    """

    opcion_orden = input(menu)

#Valido opción
    while opcion_orden not in ["1", "2", "3"]:
        print("Opción inválida")
        opcion_orden = input(menu)

#Pregunto orden ascendente o descendente
    orden = input("""
    Elija el tipo de orden:

    1. Ascendente
    2. Descendente
    """)

#Valido opción
    while orden not in ["1", "2"]:
        print("Opción inválida")
        orden = input("""
    Elija el tipo de orden:

    1. Ascendente
    2. Descendente
    """)

#Configuro reverse según la elección
    if orden == "1":
        reverse = False
    else:
        reverse = True

#Ordeno según la opción elegida
    if opcion_orden == "1":
#Ordenar por nombre
        lista_paises.sort(
            key=lambda pais: pais[0],
            reverse=reverse
        )

    elif opcion_orden == "2":
#Ordenar por población
        lista_paises.sort(
            key=lambda pais: int(pais[1]),
            reverse=reverse
        )

    elif opcion_orden == "3":
#Ordenar por superficie
        lista_paises.sort(
            key=lambda pais: int(pais[2]),
            reverse=reverse
        )

#Muestro los países ordenados
    for pais in lista_paises:
        print(pais)


ordenar_paises()