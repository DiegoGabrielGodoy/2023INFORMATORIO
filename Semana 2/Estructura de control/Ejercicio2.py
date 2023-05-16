#2-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es positivo, negativo o cero.
numero = int(input("Escriba un número entero, para saber si es positivo o no: "))
if numero >=0:
  print(numero, "Es un número positivo")
elif numero <0:
  print(numero, "Es un número negativo")