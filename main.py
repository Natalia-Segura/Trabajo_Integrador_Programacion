import csv #Importamos libreria para trabajar en archivos csv
#Funcion para agregar paises al .csv
def agregar_pais():
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
def actualizar_datos():
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
def busqueda_pais():
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

#Funcion 4

#Funcion 5

#Funcion 6

