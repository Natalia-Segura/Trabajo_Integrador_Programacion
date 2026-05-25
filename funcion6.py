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