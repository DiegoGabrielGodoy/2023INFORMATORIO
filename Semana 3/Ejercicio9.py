#Escribe un programa que pida al usuario un número y luego imprima la
#secuencia de Fibonacci correspondiente a ese número.
numero = int(input("Ingrese un número, para conocer su secuencia Fibonacci: "))
#La sucesión comienza con los números 0 y 1;2​ a partir de estos, «cada término es la suma de los dos anteriores», es la relación de recurrencia que la define.
if numero == 0:
    fibonacci = [0]
elif numero == 1:
    fibonacci = [0, 1]
else:
    fibonacci = [0, 1]
    #Calcular la secuecia de Fibonacci hasta el número dado
    for i in range(2, numero +1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) 

print (f"La secuencia de Fibonacci para el número {numero} es: {fibonacci}")
