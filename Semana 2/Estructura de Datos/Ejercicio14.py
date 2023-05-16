#Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los elementos de la tupla.

numeros = (1,2,3,4,5,)

def sumar(tupla):
    suma = 0
    for i in tupla:
        suma += i
    return suma

print(f"La suma de los números de la tupla es: {sumar(numeros)}")