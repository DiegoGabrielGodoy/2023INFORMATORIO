#Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla si contiene la letra "a".

cadena_caracter = input("Ingrese una cadena de carácteres: ")

if "a" in cadena_caracter.lower():
    print("La letra a se encuentra en la cadena de carácteres ingresada")
else:
    print("En la cadena de carácteres no se encuentra la letra a")