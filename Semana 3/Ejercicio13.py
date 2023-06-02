#Escribe un programa que pida al usuario un número y 
#luego imprima un triángulo de asteriscos con esa cantidad de filas.
numero = int(input("Ingrese un número para constriur un triángulo que contenga esa cantidad de filas: "))
triangulo = 0
print(f"El triángulo que corresponde al número {numero} es:")

for num in range(1, numero+1):
    print("*"*num)