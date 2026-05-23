import csv
#Funcion para agregar paises al .csv
def agregar_pais():
    #nuevo_pais=input("Ingrese el nombre del nuevo pais: ")
    with open("Trabajo_Integrador_Programacion/desarrollo/paises.csv", "r", newline="", encoding="UTF-8") as paises:
        lectura_diccionario=csv.DictReader(paises)
        for linea in lectura_diccionario:
            print(f"Pais: {linea['nombre']} Poblacion: {linea['poblacion']} Superficie: {linea['superficie']}km cuadrados Continente: {linea['continente']}")


agregar_pais()