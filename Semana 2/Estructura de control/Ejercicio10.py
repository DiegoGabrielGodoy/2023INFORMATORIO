#Escribir un programa que pida al usuario una letra y muestre por pantalla si es una vocal o una consonante.

vocal = {"a","e","i","o","u"}
letra = str(input("Ingrese una letra para saber si es una vocal o una consonante: "))

if letra.lower() in vocal:
    print("La letra", letra, "ingresada es una vocal")
elif not letra.isalnum() :
    print(letra, "es una carácter especial por lo tanto no corresponde a una vocal, ni tampoco a una consonante")
elif letra.isdigit() :
    print(letra, "es un número por lo tanto no corresponde a una vocal, ni tampoco a una consonante")
else:
    print("La letra", letra, "ingresada es una consonante")