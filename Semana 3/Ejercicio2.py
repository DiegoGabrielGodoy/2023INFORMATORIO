#2-Escribe un programa que pida al usuario un número y calcule la suma de todos
#Los números naturales del 1 hasta ese número.

numero = int(input("Ingrese un número entero para calcular la suma de todos los números naturales del 1 hasta ese número: "))
suma = 0

for i in range(1, numero + 1):
    suma += i

print(f"La suma de todos los números naturales desde 1 hasta {numero} es: {suma}")