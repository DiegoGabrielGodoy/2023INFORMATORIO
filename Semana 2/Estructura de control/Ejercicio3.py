#Escribir un programa que pida al usuario dos números y muestre por pantallacuál de ellos es mayor.
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese un segundo número: "))
if numero1 >= numero2:
    print(numero1, "es mayor que", numero2)
elif numero2 >= numero1:
    print(numero2, "es mayor que", numero1)  