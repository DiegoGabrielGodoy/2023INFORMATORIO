#Crea una función llamada es_capicua que tome un número como parámetro y
#devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda) 
#y False en caso contrario.

def es_capicua(numero):
    cadena = str(numero)
    if cadena == cadena[::-1]:
        return True
    else:
        return False
