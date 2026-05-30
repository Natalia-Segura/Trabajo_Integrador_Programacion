#Filtrar países por: Continente, Rango de población,Rango de superficie

def filtrar_paises():
#Creo variable del menu para no repetir
    menu = """
    Elija una opción:
    1. Continente
    2. Rango de población
    3. Rango de superficie
        """
    opcion_filtrar = input(menu)

#valido que el usuario elija una opcion dentro del menú
    while opcion_filtrar not in ["1", "2", "3"]:
        print("Opción inválida")
        opcion_filtrar = input(menu)

#pido los datos correspondientes al usuario según la opción que elija  
    if opcion_filtrar == "1":
        continente_buscado = input("Ingrese un continente: ")
    elif opcion_filtrar in ["2", "3"]:
#en el caso de la opcion 2 y 3 me aseguro que ingrese solo numeros enteros
        try:
            minimo = int(input("Ingrese el valor mínimo: "))
            maximo = int(input("Ingrese el valor máximo: "))
        except ValueError:
            print("Debe ingresar números enteros")
#Si ocurre un error termina la función
            return

#Variable para verificar si se encontraron coincidencias
    encontrado = False

#abro el archivo cvs        
    with open("paises.csv", "r", encoding="utf-8") as archivo:

        for linea in archivo:
#elimino espacios y saltos de línea y separo los datos CSV usando comas
            datos = linea.strip().split(",")
#verifico longitud de las filas            
            if len(datos) < 4:
                continue
#Evito errores por la fila de encabezado y la ignoro            
            if datos[0].lower() == "nombre":
                continue

#si el usuario elije la opción 1, busca los paises dentro de la lista que estan en ese contienente    
            if opcion_filtrar == "1":

#Busca en el indice 3(continentes) si hay coincidencias con el ingresado por el usuario                
                if datos[3].lower() == continente_buscado.lower():
#Si hay coincidencias imprime los paises que estén en el continente buscado                    
                    print(datos[0])
                    encontrado = True

            elif opcion_filtrar == "2":
#Paso el número de poblacion de string a número entero                
                poblacion = int(datos[1])
#Busco los paises dentro del rango de poblacion ingresado                
                if minimo <= poblacion <= maximo:
                    print(datos[0])
                    encontrado = True

            elif opcion_filtrar == "3":
#Paso el número de superficie de string a número entero                
                superficie = int(datos[2])
#Busco los paises dentro del rango de superficie ingresado                
                if minimo <= superficie <= maximo:
                    print(datos[0])
                    encontrado = True

#Muestra un mensaje si no hubo resultados          
        if not encontrado:
            print("No se encontraron coincidencias")

filtrar_paises()






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







#Mostrar estadísticas: País con mayor y menor población, Promedio de población, Promedio de superficie, Cantidad de países por continente

def mostrar_estadisticas():
#Abro el archivo CSV en modo lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    paises = []
#Recorro las líneas del archivo, uso [1:] para saltear el encabezado
    for linea in lineas[1:]:
#Elimino saltos de línea y separo los datos por coma
        datos = linea.strip().split(",")
#Si la línea no tiene todos los datos, se saltea
        if len(datos) < 4:
            continue
#Creo un diccionario para guardar los datos del país
        pais = {
            "nombre": datos[0],
            "continente": datos[3],
            "poblacion": int(datos[1]),
            "superficie": float(datos[2])
        }
#Agrego el país a la lista
        paises.append(pais)

#Busco el país con mayor población
    mayor = max(paises, key=lambda p: p["poblacion"])
#Busco el país con menor población
    menor = min(paises, key=lambda p: p["poblacion"])

    print("\n--- ESTADÍSTICAS ---")
#Muestro resultados de población máxima y mínima
    print("PAÍS CON MAYOR POBLACIÓN:", mayor["nombre"], mayor["poblacion"])
    print("PAÍS CON MENOR POBLACIÓN:", menor["nombre"], menor["poblacion"])

#Calculo el total de población para luego calcular el promedio
    total = sum(p["poblacion"] for p in paises)
    prom_pob = total / len(paises)
    print("\nPROMEDIO POBLACIÓN:", prom_pob)

#Calculo el total de superficie para luego calcular el promedio
    total_sup = sum(p["superficie"] for p in paises)
    prom_sup = total_sup / len(paises)
    print("PROMEDIO SUPERFICIE:", prom_sup)

#Diccionario para contar países por continente
    conteo = {}
    for p in paises:
        cont = p["continente"]
#Si el continente no existe en el diccionario, se crea
        if cont not in conteo:
            conteo[cont] = 0
#Sumo un país al continente correspondiente
        conteo[cont] += 1

    print("\nCANTIDAD DE PAÍSES POR CONTINENTE:")
#Recorro el diccionario para mostrar la cantidad de países por continente
    for cont, cant in conteo.items():
        print(cont, ":", cant)

mostrar_estadisticas()