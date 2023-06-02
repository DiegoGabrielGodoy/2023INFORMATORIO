#Crea una función llamada eliminar_duplicados que tome una lista como parámetro y 
#devuelva una nueva lista sin duplicados, conservando el orden original.

def eliminar_duplicados(cadena):
    lista = cadena.split()
    lista_sin_dupli = list(set(lista))
    return lista_sin_dupli

cadena = input("Ingrese una lista, para eliminar sus duplicados: ")
sin_duplicados = eliminar_duplicados(cadena)
print("La nueva lista sin duplicados es:")
print(sin_duplicados)