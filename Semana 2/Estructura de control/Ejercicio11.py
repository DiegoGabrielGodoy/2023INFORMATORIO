#Escribir un programa que pida al usuario dos números y muestre por pantalla la suma de ellos solo si ambos son pares.

print("Ingrese dos números pares para conocer la suma entre ellos")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    suma = (num1 + num2)
    print("El total de la suma es: ",suma)
elif num1 % 2 == 0 and num2 % 2 != 0:
    print("El número", num2, "no es par")
elif num1 % 2 != 0 and num2 % 2 == 0:
    print("El número", num1, "no es par")
else:
    print("No se pudo realizar la suma, porque los números no cumplne los requisitos de ser pares")

