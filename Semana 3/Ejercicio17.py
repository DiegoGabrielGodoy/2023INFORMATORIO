#Escribe un programa que pida al usuario una cadena de texto y 
#luego imprima la misma cadena pero con las palabras en orden inverso.

cadena = input("Ingrese una cadena de texto: ")

palabra = cadena.split()
palabra_invertida = palabra[::-1]
cadena_invertida = " ".join(palabra_invertida)
print("La cadena de texto al en orden inverso es: ")
print(cadena_invertida)
