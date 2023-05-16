#Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e imprima su índice de masa corporal (IMC).
#La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).
peso=float(input("Ingrese su peso correspondiente: "))
altura=float(input("Ingrese su altura correspondiente: "))
imc=(peso / (altura**2))
print("El indice de masa corporal (IMC) es igual a: ", imc)