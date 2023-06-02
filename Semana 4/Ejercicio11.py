#Crea una función llamada contar_vocales que tome una cadena de texto como parámetro y 
#devuelva el número de vocales que contiene.

def contar_vocales(cadena):
    conteo_vocales = 0
    for letra in cadena:
        if letra.upper() in "AEIOU":
            conteo_vocales += 1
    return conteo_vocales
        
cadena = str(input("Ingrese cadena de texto para conocer las vocales que contiene: "))
cantidad_vocales = contar_vocales(cadena)
print(f"La cadena tiene una totalidad de {cantidad_vocales} vocales") 

