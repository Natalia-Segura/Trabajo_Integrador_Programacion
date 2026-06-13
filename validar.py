def validar_entero(entero):
    try:
        entero = int(entero)
        if entero > 0:
            return True
        else:
            print("El numerodebe ser mayor que 0")
    except ValueError:
        print("Ingrese un numero entero")
    except Exception as error:
        print("\tERROR. Se produjo un error: ", type(error).__name__)
    return False

def validar_flotante(flotante):
    try:
        flotante = float(flotante)
        if flotante > 0:
            return True
        else:
            print("Ingrese un numero mayor que 0")
    except ValueError:
        print("Ingrese un numero flotante")
    except Exception as error:
        print("\tERROR. Se produjo un error: ", type(error).__name__)
    return False

def validar_texto(palabra):
    separar=palabra.split()
    for i in separar:
        if i.isalpha() == True:
            pass
        else:
            return False
    return True
