#Escribe un programa que pida al usuario un número y 
#Luego imprima un triángulo de números como el siguiente:
#1
#2 3
#4 5 6
#7 8 9 10
numero = int(input("Ingrese un número para construir un triángulo que contenga esa cantidad: "))
print(f"El triángulo que corresponde al número {numero} es:")

num = 1
for i in range(1, numero + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
