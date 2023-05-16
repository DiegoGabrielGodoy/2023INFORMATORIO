#Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es múltiplo de 2 y de 3 a la vez.
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0 and numero % 3 == 0:
    print(numero, "es múltiplo de 2 y de 3 a la vez")
elif numero % 2 == 0 and numero % 3 != 0:
    print(numero, "es múltiplo de 2, pero no de 3")
elif numero % 2 != 0 and numero % 3 == 0:
    print(numero, "no es múltiplo de 2, pero si de 3")
else:
    print(numero, "no es múltiplo de 2 y tampoco es múltiplo de 3")