#7-Escribe un programa que pida al usuario una palabra y determine si es un palíndromo 
#(es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).

palabra = input("Escribe una palabra para saber si es palindrómica o no: ")

if palabra.lower() == palabra.lower()[::-1]:
    print (f"{palabra} es una palabra palindrómica")
else:
    print (f"{palabra} no es una palabra palindrómica")
