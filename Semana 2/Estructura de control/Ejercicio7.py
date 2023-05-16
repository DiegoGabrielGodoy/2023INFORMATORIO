#Escribir un programa que pida al usuario un carácter y muestre por pantalla si
#es una letra mayúscula, una letra minúscula, un número o un carácter especial.
caracter = input("Ingrese un carácter: ")

if caracter.isupper():
    print(caracter, "es una letra mayúscula")
elif caracter.islower():
    print(caracter, "es una letra minúscula")
elif caracter.isdigit():
    print(caracter, "es un número")
else:
    print(caracter, "es un caracter especial")