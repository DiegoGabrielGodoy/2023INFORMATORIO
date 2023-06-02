#Escribe un programa que pida al usuario una cadena de texto y luego imprima
#el número de palabras que contiene.

cadena = input("Ingrese una cadena de texto: ")

palabra = cadena.split()
cantidad_palabras = len(palabra)

print(f"La cantidad de palabras que contiene la cadenad de texto es: {cantidad_palabras}")