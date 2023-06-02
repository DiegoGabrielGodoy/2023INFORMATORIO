#Crea una función llamada contar_palabras que tome una cadena de texto
#como parámetro y devuelva el número de palabras que contiene. Se considera
#que las palabras están separadas por espacios.

def contar_palabras(cadena):
    cadena_texto = cadena.split()
    total_palabras = len(cadena_texto)
    return total_palabras

cadena = input("Ingrese una cadena de texto, para conocer la cantidad de palabras que contiene: ")
total = contar_palabras(cadena)
print(f"La cantidad de palabras que se encuentran en la cadena son: {total}")