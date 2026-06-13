#Importamos libreria para trabajar en archivos csv
import csv
import validar

#Funcion para agregar paises al .csv
def agregar_pais(): #Opcion 1
    condi_1=False #Condicion para verificar que no se repita pais
    
    while True:
        nuevo_pais=input("Ingrese el nombre del nuevo pais: ").capitalize()
        validar_texto=validar.validar_texto(nuevo_pais)
        if validar_texto:
            break
        else:
            print("\tERROR. Ingrese una cadena de texto")
    # Verifica que el país no exista previamente en el archivo
    with open("data/paises.csv", "r", newline="", encoding="UTF-8") as paises: 
        lectura_diccionario=csv.DictReader(paises) #Lee el csv y guarda las filas en un diccionario, crea un iterador
        for linea in lectura_diccionario: 
            if linea['nombre'] == nuevo_pais: 
                condi_1 = True 
    #Cerramos el csv
    if condi_1 == False:
        # Solicita y valida la población
        with open("data/paises.csv", "a", newline="", encoding="UTF-8") as paises: 
            lectura_lista=csv.writer(paises) #Se crea un objecto escritor y se guarda en la variable
            #Solicita y calida la poblacion
            while True:
                poblacion = input(f"Ingrese la cantidad de poblacion de {nuevo_pais}: ")
                validar_entero=validar.validar_entero(poblacion)
                if validar_entero:
                    break
            # Solicita y valida la superficie 
            while True: 
                superficie = input("Ingrese la superficie: ")
                validar_flotante = validar.validar_flotante(superficie)
                if validar_flotante:
                    break
            # Solicita y valida el continente 
            while True:
                continente=input("Ingrese el continente: ").capitalize()
                validar_texto=validar.validar_texto(continente)
                if validar_texto:
                    break
            # Agrega el nuevo registro al archivo 
            lectura_lista.writerow([nuevo_pais,poblacion,superficie,continente]) #Escribimos una nueva fila al final del csv
        
    else:
        print("\tERROR. El pais ya se encuentra en el archivo .csv") 

#Funcion para actualizar poblacion y superficie
def actualizar_datos(): #Opcion 2
    condi_2=False
    lista_paises=[] 
    encabezado=["nombre","poblacion","superficie","continente"] 
    # Solicita y valida el nombre del pais a modificar
    while True: 
            pais=input("A que pais desea actualizar sus datos? ").capitalize()
            validar_texto=validar.validar_texto(pais)
            if validar_texto:
                break
    # Carga los registros del CSV en una lista de diccionarios 
    with open("data/paises.csv","r",newline="",encoding="UTF-8") as lista: 
        paises_diccionario=csv.DictReader(lista) #Convierte las filas del csv en diccionario, usa la primera linea como claves
        
        for list_pais in paises_diccionario: #Lista de diccionarios
            lista_paises.append(list_pais) 
        
        # Verifica si el país existe en el archivo 
        for buscar in lista_paises:
            if buscar['nombre'] == pais:
                condi_2=True
                break 
    
    # Si el país existe permite modificar sus datos 
    if condi_2 == True: 
        with open("data/paises.csv","w",newline="",encoding="UTF-8") as paises: 
            diccionario_pais=csv.DictWriter(paises, fieldnames=encabezado) #Creacion del escritor y establecemos el orden de las columnas
            
            for clave in lista_paises: #Recorremos la lista de diccionarios
                if clave['nombre'] == pais: 
                    
                    # Permite actualizar la poblacion 
                    while True: 
                        poblacion=input(f"La cantidad de poblacion de {pais} es {clave['poblacion']}, desea actualizar?: ('S' Actualizar | 'N' No hacer nada)\n>>>:  ").upper() 
                        
                        match poblacion: 
                            case "S": 
                                nueva_poblacion = input("Ingrese la nueva poblacion: ")
                                validar_entero=validar.validar_entero(nueva_poblacion)
                                if validar_entero:
                                    break
                            case "N":
                                break 
                            case _: 
                                print("\tERROR. Ingrese S o N")
                    
                    # Permite actualizar la superficie 
                    while True: 
                        superficie=input(f"La cantidad de superficie de {pais} es {clave['superficie']}, desea actualizar?: ('S' Actualizar | 'N' No hacer nada)\n>>>:  ").upper() 
                        match superficie: 
                            case "S": 
                                nueva_superficie = input("Ingrese la nueva superficie: ")
                                validar_flotante=validar.validar_flotante(nueva_superficie)
                                if validar_flotante:
                                    break
                            case "N": 
                                break 
                            case _: 
                                print("\tERROR. Ingrese S o N")
            # Guarda los cambios realizados en el archivo
            diccionario_pais.writeheader() #Escribe los encabezados
            diccionario_pais.writerows(lista_paises) #Recorre los diccionarios que estan en la lista y los escribe 
            print("Datos actualizados correctamente!")
    else:
        print(f"\tERROR. {pais} no se encuentra") #Si no se encuentra el pais que se escribio