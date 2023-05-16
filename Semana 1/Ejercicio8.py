#Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159.
pi=3.1459
radio=float(input("Ingrese el radio del círculo: "))
print("El diametro del círculo es: ", (2*radio))
print("La circunferencia del circulo es: ", (2*pi*radio))
print("El área del círculo es: ", (pi*(radio**2)))
