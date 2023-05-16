#Escribir un programa que pida al usuario tres números y muestre por pantalla el mayor de ellos.

print("Ingrese tres números para saber cual de ellos es el mayor")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: ")) 
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El número", num1, "es mayor que los números", num2, "y", num3)
elif num2 > num1 and num2 > num3:
    print("El número", num2, "es mayor que los números", num1, "y", num3)
elif num3 > num1 and num3 > num2:
    print("El número", num3, "es mayor que los números", num1, "y", num2)
else:
    print("Todos los números son iguales")