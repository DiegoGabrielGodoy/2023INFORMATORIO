#Escribe un programa que pida al usuario un número y calcule su factorial.
numero = int(input("Ingrese un número para calcular su factorial: "))
#Un factorial es el producto que resulta de multiplicar un número entero positivo
if numero == 0:
    factorial = 1
    print (f"El valor del factorial para el número {numero} es: 1")
elif numero > 0:
    factorial = 1
    for i in range (1 , numero +1):
        factorial *= i
    print (f"El valor del factorial para el número {numero} es: {factorial}")
else:
    print("El número debe ser mayor o igual a cero para calcular el factorial.")
