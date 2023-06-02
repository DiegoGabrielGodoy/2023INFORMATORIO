#Crea una función llamada encontrar_maximo que tome una lista de números
#como parámetro y devuelva el número máximo de la lista.

def encontrar_maximo(numeros):
    lista = numeros.split()
    if len(lista) == 0:
        return None
    else:
        lista_numeros = [int(num) for num in lista]
        maximo = max(lista_numeros)
    return maximo

numeros = input("Ingrese una lista de números separados por espacios: ")
numero_maximo = encontrar_maximo(numeros)
print(f"El valor máximo de los números que se encuentran en la lista es: {numero_maximo}")