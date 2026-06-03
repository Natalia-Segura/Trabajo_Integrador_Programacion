import csv #Importamos libreria para trabajar en archivos csv

#Funcion para agregar paises al .csv
def agregar_pais(): #Opcion 1
    condi_1=False #Condicion para no agregar un pais que existe en la lista de paises
    while True:
        nuevo_pais=input("Ingrese el nombre del nuevo pais: ").capitalize() #Nuevo pais que el usuario desea ingresar
        if nuevo_pais.isalpha() == True:
            break
        else:
            print("\tERROR. Ingrese una cadena de texto")
    with open("paises.csv", "r", newline="", encoding="UTF-8") as paises: #Abrimos el archivo csv en modo "r" que es lectura
        lectura_diccionario=csv.DictReader(paises) #El archivo csv se mapea directamente en un diccionario
        for linea in lectura_diccionario: #Recorremos el diccionario con el bucle
            if linea['nombre'] == nuevo_pais: #Si el valor de la clave que recorre el diccionario es igual al pais que ingreso el usuario se cambia la condicion
                condi_1 = True #La condicion se hace verdadera si se llega a encontrar un pais repetido
    #El archivo csv se cierra
    if condi_1 == False: #En caso que no encontro niuna concidencia en el diccionario
        with open("paises.csv", "a", newline="", encoding="UTF-8") as paises: #Abrimos el archivo csv en modo "a" que permite agregar elementos al final del archivo
            lectura_lista=csv.writer(paises) #Preparamos el archivo para escribir en el
            while True: #Bucle para agregar la cantidad de poblacion, debe ser un numero entero
                poblacion=input(f"Ingrese la cantidad de poblacion de {nuevo_pais}: ")
                try: #Se intenta convertir a entero
                    poblacion = int(poblacion)
                    if poblacion > 0: #Condicion para que sea un numero mayor a 0
                        break #Si es un numero entero y mayor a 0 se sale del bucle
                    else:
                        print("\tERROR. El numero debe ser mayor a 0")
                except ValueError: #Exepcion si no se pudo convertir en entero
                    print("\tERROR. Debe ingresar un numero entero")
                except Exception as error: #Es nuestra barrera de seguidad, captira cualquier exepcion
                    print("\tERROR. Se produjo un error: ", type(error).__name__) #Se muestra el tipo de exepcion
            while True: #Bucle para agregar la cantidad de superficie, debe ser un numero flotante
                superficie=input("Ingrese la superficie (en km cuadrados): ")
                try: #Intenta convertir a flotante
                    superficie = float(superficie)
                    if superficie > 0: #Condicion para que el numero flotante sea mayor a 0
                        break
                    else:
                        print("\tERROR. Debe ingresar un numero positivo")
                except ValueError: #exepcion si no se pudo convertir en flotante
                    print("\tERROR. Ingrese un numero flotante")
                except Exception as error: #Se toma otro tipo de error imprevisto
                    print("\tERROR. Se produjo un error: ", type(error).__name__) #Se muestra el tipo de error
            while True: #Bucle para agregar el continente
                continente=input("Ingrese el continente: ").capitalize()
                if continente.isalpha() == True: #Dondicion para ver si se ingreso una cadena de texto
                    break
                else:
                    print("\tERROR. Ingrese una cadena de texto")
            lectura_lista.writerow([nuevo_pais,poblacion,superficie,continente]) #Recibe una lista y la agrega como una sola linea al final del archivo csv
        #El archivo csv se cierra
    else:
        print("\tERROR. El pais ya se encuentra en el archivo .csv") #Si encuentra una concidencia, no abre el archivo y se notifica que el pais existe


            #Funcion para actualizar poblacion y superficie
def actualizar_datos(): #Opcion 2
    condi_2=False #Variable booleana para encontrar pais
    lista_paises=[] #Lista vacia para guardar diccionarios del archivo csv
    encabezado=["nombre","poblacion","superficie","continente"] #Encabezado para la actualizacion del archivo csv
    while True: #Bucle para ingresar el nombre
            pais=input("A que pais desea actualizar sus datos? ").capitalize()
            if pais.isalpha() == True: #Validacion para ver si se ingreso una cadena de texto
                break #Si se ingreso una cadena de texto se sale del bucle
            else:
                print("\tERROR. Ingrese una cadena de texto")
    with open("paises.csv","r",newline="",encoding="UTF-8") as lista: #Abrimos el archivo csv en modo lectura
        paises_diccionario=csv.DictReader(lista) #Mapeamos cada fila del archivo csv a un diccionario, DictReader entiende que la primera linea es un encabezado
        for list_pais in paises_diccionario: #Recorremos el diccionario
            lista_paises.append(list_pais) #Lo agregamos a la lista, para tener una lista de diccionarios
        for buscar in lista_paises: #Realizamos la busqueda del pais que se el ususario ingreso
            if buscar['nombre'] == pais: #Si el valor del elemento del diccionario es igual al pais que ingresa el usuario, la variable booleana es 'True'
                condi_2=True
                break #Interrupimos el bucle for cuando tenemos coincidencia
    if condi_2 == True: #En caso de encontrar el pais se ejecuta la siguiente condicion
        with open("paises.csv","w",newline="",encoding="UTF-8") as paises: #Abrimos el csv en modo de escritura
            diccionario_pais=csv.DictWriter(paises, fieldnames=encabezado) #Escribirmos diccionarios en el archivo csv, y le indicamos cual es su encabezado con fieldnames
            for clave in lista_paises: #Volvemos a utilizar la lista con diccionarios, y la recorremos
                if clave['nombre'] == pais: #Buscamos la clave que el usuario solicito
                    while True: #Bucle para la modificacion de la cantidad de poblacion (debe se run numero entero)
                        poblacion=input(f"La cantidad de poblacion de {pais} es {clave['poblacion']}, desea actualizar?: ('S' Agregar | 'N' No agregar)\t>>>:  ").upper() #Se muestra la cantidad de poblacion del pais, y se le pregunta si quiere editar
                        match poblacion: #Mini menu para editar o no
                            case "S": #En caso de querer editar
                                nueva_poblacion=input("Ingrese el nuevo valor de la pobalcion: ") 
                                try:
                                    nueva_poblacion = int(nueva_poblacion) #Intentamos convertir en entero el numero que ingreso el usuario
                                    clave['poblacion'] = nueva_poblacion #Si es un entero, se actualiza el valor
                                    print(f"Poblacion de {pais} actualizada") #Se muestra mensaje de que se actualizo
                                    break #Salimos del buble para la modificacion de poblacion
                                except ValueError: #Si el usuario ingresa un flotante, una cadena de texto o no agrega nada 
                                    print("\tERROR. Ingrese un numero entero")
                                except Exception as error: #Si se tiene otro tipo de exepcion
                                    print("\tERROR. Se detecto un error ",type(error).__name__) #Se muestra que tipo de exepcion es
                            case "N": #En caso de no querer editar
                                break #Salimos del buble para la modificacion de poblacion ya que no se queiere editar
                            case _: #Si se ingresa cualquier letra o cadena de texto
                                print("\tERROR. Ingrese S o N")
                    while True: #Bucle para modificar la superficie (flotante)
                        superficie=input(f"La cantidad de superficie de {pais} es {clave['superficie']}, desea actualizar?: ('S' Agregar | 'N' No agregar)\t>>>:  ").upper() #Se muestra la cantidad de superficie, y se pregunta si quiere editar
                        match superficie: #Mini menu
                            case "S": #Si se quiere cambiar la superficie
                                nueva_superficie=input("Ingrese el nuevo valor de la superficie: ")
                                try:
                                    nueva_superficie = float(nueva_superficie) #Intetamos pasar a flotante
                                    clave['superficie'] = nueva_superficie #Si es un flotante actualizamos 
                                    print(f"Superficie de {pais} actualizada") #Se muestra mensaje que el cambio fue exitoso
                                    break #Salimos del bucle
                                except ValueError: #Si se ingresa cualquier caracter que no sea un flotante
                                    print("\tERROR. Ingrese un numero flotante")
                                except Exception as error: #Si se encuentra otra exepcion se guarda
                                    print("\tERROR. Se detecto un error ",type(error).__name__) #Se muestra que tipo de exepcion se encontro
                            case "N": #Si no se quiere cambiar la superficie
                                break #Salimos del bucle
                            case _: #Si se ingresa una letra o cadena de texto 
                                print("\tERROR. Ingrese S o N")
            diccionario_pais.writeheader() #Escribe en el archivo csv en la primera fila el encabezado
            diccionario_pais.writerows(lista_paises) #Escribie todas las filas en el archivo csv
    else:
        print(f"\tERROR. {pais} no se encuentra") #Si no se encuentra el pais que se escribio

            #Funcion para buscar un pais o su coincidencia
def busqueda_pais(): #Opcion 3
    lista=[] #Lista vacia para guardar los datos del csv
    condi_1=False #Variable booleana para ver si se encontro el pais o su coincidencia
    pais=input("Que pais desea buscar?: ").capitalize()
    if pais.isalpha() == True: #Si se ingreso una cadena de texto
        with open("paises.csv","r",newline="",encoding="UTF-8") as paises:
            lista_pais=csv.DictReader(paises) #Permite ver el archivo csv en diccionarios mientra se recorre uno por un con un for
            for nombres in lista_pais: #Guardamos los diccionarios en una lista
                lista.append(nombres)
            for busqueda in lista: #Recorrido para buscar el pais
                if pais == busqueda['nombre']: #Si coincide el nombre entero
                    print(f"El pais {pais} se encuentra en la lista")
                    condi_1=True #Bandera para indicar que se encontro pais por nombre completo
                    break #Salimos del for
                elif pais in busqueda['nombre']: #Se busca la coincidencia
                    print(f"El pais {busqueda['nombre']} se cuentra en la lista")
                    condi_1=True #Bandera para indicar que la coincidencia se encontro
                    break #Salimos del for
        if condi_1 == False: #Si no se encontro por nombre completo ni por coincidencia
            print("El pais no se encuentra en la lista")
    else: #Si no se ingresa una cadena de texto
        print("\tERROR. Ingrese una cadena de texto")
            #Filtrar países por: Continente, Rango de población,Rango de superficie
def filtrar_paises(): #Opcion 4
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

            # Ordenar países por: Nombre, Población, Superficie (ascendente o descendente)
def ordenar_paises(): #Opcion 5

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
            #Mostrar estadísticas: País con mayor y menor población, Promedio de población, Promedio de superficie, Cantidad de países por continente
def mostrar_estadisticas(): #Opcion 6
#Abro el archivo CSV en modo lectura
    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
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
    match opcion:
<<<<<<< HEAD

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
=======
        case 0:
            print("Usted salio del programa")
>>>>>>> 1b63454c1ffe63cf13dcb8e45ee45c2c27b3ddaa
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