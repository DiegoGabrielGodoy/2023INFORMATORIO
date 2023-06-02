#Escribe un programa que pida al usuario una palabra y luego imprima la misma
#palabra pero con las letras en orden inverso.

palabra = input("Ingrese una palabra: ")

for letra in (palabra[::-1]):
    print(letra) 
    