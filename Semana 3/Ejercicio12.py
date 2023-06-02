#Escribe un programa que pida al usuario una lista de números separados por comas y calcule su promedio.
print("Ingrese una lista de números separados por comas para conocer su promedio: ")
ingreso = input()
lista = ingreso.split(',')

suma = 0
for num in lista:
    suma += int(num)
    n = len(lista)
    promedio = suma / n
print(f"El promedio de los números en la lista es: {promedio}")

