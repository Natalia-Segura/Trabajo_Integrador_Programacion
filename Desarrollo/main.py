import csv #Importamos libreria para trabajar en archivos csv
#Funcion para agregar paises al .csv
def agregar_pais():
    condi_1=False #Condicion para no agregar un pais que existe en la lista de paises
    nuevo_pais=input("Ingrese el nombre del nuevo pais: ").capitalize() #Nuevo pais que el usuario desea ingresar
    with open("Trabajo_Integrador_Programacion/desarrollo/paises.csv", "r", newline="", encoding="UTF-8") as paises: #Abrimos el archivo csv en modo "r" que es lectura
        lectura_diccionario=csv.DictReader(paises) #El archivo csv se mapea directamente en un diccionario
        for linea in lectura_diccionario: #Recorremos el diccionario con el bucle
            if linea['nombre'] == nuevo_pais: #Si el valor de la clave que recorre el diccionario es igual al pais que ingreso el usuario se cambia la condicion
                condi_1 = True #La condicion se hace verdadera si se llega a encontrar un pais repetido
    #El archivo csv se cierra
    if condi_1 == False: #En caso que no encontro niuna concidencia en el diccionario
        with open("Trabajo_Integrador_Programacion/desarrollo/paises.csv", "a", newline="", encoding="UTF-8") as paises: #Abrimos el archivo csv en modo "a" que permite agregar elementos al final del archivo
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
