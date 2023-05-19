#Escribe un programa que imprima la suma de todos los números pares del 1 al 100.

suma = 0

for numero in range (2, 101, 2):
    suma += numero

print(f"La suma de los numeros pares del 1 al 100 es: {suma}")