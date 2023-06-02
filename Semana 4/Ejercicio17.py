#Crea una función llamada es_anagrama que tome dos cadenas de texto como parámetros y 
#devuelva True si son anagramas (es decir, si tienen las mismas
#letras pero en distinto orden), o False en caso contrario.

def es_anagrama(cadena1, cadena2):
    if sorted(cadena1) == sorted(cadena2):
        return "Es anagrama"
    else:
        return "No es anagrama"

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

anagrama = es_anagrama(cadena1, cadena2)
print(anagrama)