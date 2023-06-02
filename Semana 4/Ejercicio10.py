#Crea una función llamada calcular_factorial que tome un número entero como parámetro y 
#devuelva el factorial de ese número. El factorial de un número entero positivo n 
#se define como el producto de todos los números enteros positivos desde 1 hasta n.

def calcular_factorial(num):
    if num == 0:
        factorial = 1
        print (f"El valor del factorial para el número {num} es: 1")
    elif num > 0:
        factorial = 1
        for i in range (1 , num +1):
            factorial *= i 
        return factorial
    else:
        print("El número debe ser mayor o igual a cero para calcular el factorial.")


num = int(input("Ingrese un número para calcular su factorial: "))
factorial = calcular_factorial(num)
if factorial is not None:
    print(f"El valor del factorial para el número {num} es: {factorial}")