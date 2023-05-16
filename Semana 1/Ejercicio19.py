#Escribe un programa que solicite al usuario un número decimal y luego imprima la parte entera y decimal por separado.
numero=float(input("Ingrese un número decimal: "))
numero_entero = int(numero)
numero_decimal = numero - numero_entero
print("El número entero es: ", numero_entero)
print("El numero en decimales es: ", numero_decimal)
