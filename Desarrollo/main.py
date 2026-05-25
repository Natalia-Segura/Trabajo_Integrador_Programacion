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