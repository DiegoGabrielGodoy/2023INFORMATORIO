#Escribe un programa que pida al usuario una cadena de texto y 
#luego imprima la misma cadena pero con cada palabra al revés.

cadena = input("Ingrese una cadena de texto: ")

print("La cadena de texto al reves es: ")

lista_cadena = list(cadena)
lista_cadena.reverse()
cadena_al_reves = "".join(lista_cadena)
print(cadena_al_reves)