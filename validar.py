def validar_entero(entero):
    try:
        entero = int(entero)
        return True
    except ValueError:
        print("Ingrese un numero entero")
    return False

def validar_flotante():
    pass

def validar_texto(palabra):
    separar=palabra.split()
    for i in separar:
        if i.isalpha() == True:
            pass
        else:
            return False
    return True
