#3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
#multiplicar correspondiente a ese número del 1 al 10.

numero = int(input("Ingrese un número para saber su tabla de multiplicar correspondiente: "))
print(f"La tabla de multiplicación correspondiente al número {numero} es: ")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")