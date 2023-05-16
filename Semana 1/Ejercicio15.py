#Escribe un programa que solicite al usuario una temperatura en grados Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
#La fórmula para convertir de Celsius a Fahrenheit es: F=(C * 1.8) + 32
c=float(input("Ingrese la temperatura en grados Celsius, para conocer su equivalente en Fahrenheit: "))
f=(c * 1.8) + 32
print("Los ", c, "grados Celsius equivalen a ", f, "grados Fahrenheit")