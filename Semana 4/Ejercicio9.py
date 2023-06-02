#Crea una función llamada promedio que tome una lista de números como parámetro y
#devuelva el promedio de esos números.

def promedio(lista_numeros):
    if len(lista_numeros) == 0:
        return None
    
    total = sum(lista_numeros)
    promedio = total / len(lista_numeros)
    return promedio

numeros = input("Ingrese una lista de números separados por espacios: ")
cadena = numeros.split()
lista_numeros = [int(numero) for numero in cadena]
promedio_numeros = promedio(lista_numeros)
print(f"El promedio de los números es: {promedio_numeros}")

