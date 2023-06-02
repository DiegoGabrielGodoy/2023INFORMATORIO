#Escribe un programa que pida al usuario un número y luego imprima un triángulo de números como el siguiente:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

numero = int(input("Ingrese un número para constriur un triángulo que contenga esa cantidad de filas: "))
print(f"El triángulo que corresponde al número {numero} es:")

for num in range(1, numero + 1):
    for i in range(num):
        print(num, end=" ")
    print()

