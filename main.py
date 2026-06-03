while True:
    opcion = input("""
    1. Agregar país
    2. Actualizar país
    3. Buscar país
    4. Filtrar países
    5. Ordenar países
    6. Estadísticas
    0. Salir
    """)

    match opcion:

        case "1":
#Importamos libreria para trabajar en archivos csv
            import csv 
            
            #Funcion para agregar paises al .csv
            def agregar_pais():
                condi_1=False  
                
                while True:
                    nuevo_pais = input("Ingrese el nombre del nuevo pais: ").capitalize()
                    
                    if nuevo_pais.isalpha() == True:
                        break
                    else:
                        print("\tERROR. Ingrese una cadena de texto")

                # Verifica que el país no exista previamente en el archivo
                with open("paises.csv", "r", newline="", encoding="UTF-8") as paises:
                    lectura_diccionario=csv.DictReader(paises)
                    
                    for linea in lectura_diccionario:
                        
                        if linea['nombre'] == nuevo_pais:
                            condi_1 = True 

                if condi_1 == False: 
                    
                    # Solicita y valida la población
                    with open("paises.csv", "a", newline="", encoding="UTF-8") as paises: 
                        
                        lectura_lista=csv.writer(paises) 
                        
                        while True: 
                            poblacion=input(f"Ingrese la cantidad de poblacion de {nuevo_pais}: ")
                            
                            try: 
                                poblacion = int(poblacion)
                                if poblacion > 0:
                                    break 
                                else:
                                    print("\tERROR. El numero debe ser mayor a 0")
                            
                            except ValueError: 
                                print("\tERROR. Debe ingresar un numero entero")
                            
                            except Exception as error: 
                                print("\tERROR. Se produjo un error: ", type(error).__name__) 
                        
                        # Solicita y valida la superficie
                        while True: 
                            superficie=input("Ingrese la superficie (en km cuadrados): ")
                            
                            try:
                                superficie = float(superficie)
                                
                                if superficie > 0: 
                                    break
                                else:
                                    print("\tERROR. Debe ingresar un numero positivo")
                            
                            except ValueError: 
                                print("\tERROR. Ingrese un numero flotante")
                            
                            except Exception as error: 
                                print("\tERROR. Se produjo un error: ", type(error).__name__) 
                        
                        # Solicita y valida el continente
                        while True: 
                            continente=input("Ingrese el continente: ").capitalize()
                            
                            if continente.isalpha() == True: 
                                break
                            else:
                                print("\tERROR. Ingrese una cadena de texto")
                        
                        # Agrega el nuevo registro al archivo
                        lectura_lista.writerow([nuevo_pais,poblacion,superficie,continente]) 
                    
                else:
                    print("\tERROR. El pais ya se encuentra en el archivo .csv") 

            agregar_pais()

        case "2":
#Funcion para actualizar poblacion y superficie

            def actualizar_datos():

                condi_2=False 
                lista_paises=[] 
                encabezado=["nombre","poblacion","superficie","continente"] 

                # Solicita y valida el nombre del pais a modificar
                while True: 
                        pais=input("A que pais desea actualizar sus datos? ").capitalize()
                        
                        if pais.isalpha() == True: 
                            break 
                        else:
                            print("\tERROR. Ingrese una cadena de texto")

                # Carga los registros del CSV en una lista de diccionarios
                with open("paises.csv","r",newline="",encoding="UTF-8") as lista: 

                    paises_diccionario=csv.DictReader(lista) 

                    for list_pais in paises_diccionario: 
                        lista_paises.append(list_pais) 

                    # Verifica si el país existe en el archivo
                    for buscar in lista_paises: 

                        if buscar['nombre'] == pais: 
                            condi_2=True
                            break 

                # Si el país existe permite modificar sus datos
                if condi_2 == True: 

                    with open("paises.csv","w",newline="",encoding="UTF-8") as paises: 
                        diccionario_pais=csv.DictWriter(paises, fieldnames=encabezado)

                        for clave in lista_paises:
                            if clave['nombre'] == pais: 

                                # Permite actualizar la poblacion
                                while True: 
                                    poblacion=input(f"La cantidad de poblacion de {pais} es {clave['poblacion']}, desea actualizar?: ('S' Agregar | 'N' No agregar)\t>>>:  ").upper() 
                                    
                                    match poblacion: 
                                        case "S": 
                                            nueva_poblacion=input("Ingrese el nuevo valor de la pobalcion: ") 
                                            
                                            try:
                                                nueva_poblacion = int(nueva_poblacion) 
                                                clave['poblacion'] = nueva_poblacion 
                                                print(f"Poblacion de {pais} actualizada") 
                                                break 
                                            
                                            except ValueError: 
                                                print("\tERROR. Ingrese un numero entero")
                                            
                                            except Exception as error: 
                                                print("\tERROR. Se detecto un error ",type(error).__name__) 
                                        
                                        case "N": 
                                            break 
                                        
                                        case _: 
                                            print("\tERROR. Ingrese S o N")

                                # Permite actualizar la superficie
                                while True: 
                                    superficie=input(f"La cantidad de superficie de {pais} es {clave['superficie']}, desea actualizar?: ('S' Agregar | 'N' No agregar)\t>>>:  ").upper()

                                    match superficie: 
                                        case "S": 
                                            nueva_superficie=input("Ingrese el nuevo valor de la superficie: ")

                                            try:
                                                nueva_superficie = float(nueva_superficie) 
                                                clave['superficie'] = nueva_superficie  
                                                print(f"Superficie de {pais} actualizada") 
                                                break 

                                            except ValueError: 
                                                print("\tERROR. Ingrese un numero flotante")

                                            except Exception as error: 
                                                print("\tERROR. Se detecto un error ",type(error).__name__) 

                                        case "N": 
                                            break 

                                        case _: 
                                            print("\tERROR. Ingrese S o N")

                        # Guarda los cambios realizados en el archivo
                        diccionario_pais.writeheader() 
                        diccionario_pais.writerows(lista_paises) 

                else:
                    print(f"\tERROR. {pais} no se encuentra") 

            actualizar_datos()


        case "3":
#Funcion para buscar un pais o su coincidencia

            def busqueda_pais():

                lista=[] 
                condi_1 = False 

                pais = input("Que pais desea buscar?: ").capitalize()

                if pais.isalpha() == True: 

                    # Carga los registros del CSV para realizar la búsqueda
                    with open("paises.csv","r",newline="",encoding="UTF-8") as paises:

                        # Permite ver el archivo csv en diccionarios mientra se recorre uno por un con un for
                        lista_pais=csv.DictReader(paises) 

                        for nombres in lista_pais: 
                            lista.append(nombres)

                        # Busca coincidencia exacta o parcial del nombre ingresado
                        for busqueda in lista: 

                            if pais == busqueda['nombre']: 
                                print(f"El pais {pais} se encuentra en la lista")
                                condi_1=True 
                                break 

                            elif pais in busqueda['nombre']: 
                                print(f"El pais {busqueda['nombre']} se cuentra en la lista")
                                condi_1 = True
                                break 

                    #Si no se encontro por nombre completo ni por coincidencia
                    if condi_1 == False: 
                        print("El pais no se encuentra en la lista")

                else: 
                    print("\tERROR. Ingrese una cadena de texto")

            busqueda_pais()


        case "4":
#Filtrar países por: Continente, Rango de población,Rango de superficie

            def filtrar_paises():
            # Creo variable del menu para no repetir
                menu = """
                Elija una opción:
                1. Continente
                2. Rango de población
                3. Rango de superficie
                    """
                opcion_filtrar = input(menu)

            # Valido que el usuario elija una opcion dentro del menú
                while opcion_filtrar not in ["1", "2", "3"]:
                    print("Opción inválida")
                    opcion_filtrar = input(menu)

            # Pido los datos correspondientes al usuario según la opción que elija  
                if opcion_filtrar == "1":
                    continente_buscado = input("Ingrese un continente: ")
                elif opcion_filtrar in ["2", "3"]:
            # En el caso de la opcion 2 y 3 me aseguro que ingrese solo numeros enteros
                    try:
                        minimo = int(input("Ingrese el valor mínimo: "))
                        maximo = int(input("Ingrese el valor máximo: "))
                    except ValueError:
                        print("Debe ingresar números enteros")
            # Si ocurre un error termina la función
                        return

            # Variable para verificar si se encontraron coincidencias
                encontrado = False

            # Abro el archivo cvs        
                with open("paises.csv", "r", encoding="utf-8") as archivo:

                    for linea in archivo:
            # Elimino espacios y saltos de línea y separo los datos CSV usando comas
                        datos = linea.strip().split(",")
            # Verifico longitud de las filas            
                        if len(datos) < 4:
                            continue
            # Evito errores por la fila de encabezado y la ignoro            
                        if datos[0].lower() == "nombre":
                            continue

            # Si el usuario elije la opción 1, busca los paises dentro de la lista que estan en ese contienente    
                        if opcion_filtrar == "1":

            # Busca en el indice 3(continentes) si hay coincidencias con el ingresado por el usuario                
                            if datos[3].lower() == continente_buscado.lower():
            # Si hay coincidencias imprime los paises que estén en el continente buscado                    
                                print(datos[0])
                                encontrado = True

                        elif opcion_filtrar == "2":
            # Paso el número de poblacion de string a número entero                
                            poblacion = int(datos[1])
            # Busco los paises dentro del rango de poblacion ingresado                
                            if minimo <= poblacion <= maximo:
                                print(datos[0])
                                encontrado = True

                        elif opcion_filtrar == "3":
            # Paso el número de superficie de string a número entero                
                            superficie = int(datos[2])
            # Busco los paises dentro del rango de superficie ingresado                
                            if minimo <= superficie <= maximo:
                                print(datos[0])
                                encontrado = True

            # Muestra un mensaje si no hubo resultados          
                    if not encontrado:
                        print("No se encontraron coincidencias")

            filtrar_paises()


        case "5":
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

        case "6":
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


        case "0":
            break

        case _:
            print("Opción inválida")