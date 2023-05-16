#Desafio 2:Escribe un programa que solicite al usuario su información personal, incluyendo
#su nombre completo, edad, estatura, peso, dirección y número de teléfono.
#A continuación, el programa deberá imprimir un mensaje con los datos
#ingresados por el usuario en el siguiente formato:
#La información ingresada es la siguiente:
#Nombre completo: [nombre completo]
#Edad: [edad]
#Estatura: [estatura] cm
#Peso: [peso] kg
#Dirección: [dirección]
#Número de teléfono: [número de teléfono]
nombre_completo=str(input("Ingrese su nombre completo: "))
edad=int(input("Ingrese su edad: "))
estatura=float(input("Ingrese su altura en centímetros: "))
peso=float(input("Ingrese su peso en Kilogramos: "))
direccion=str(input("Ingrese su direccion: "))
numero_telefonico=int(input("Ingrese su número telefonico: "))
print("La informacion personal del solicitante es:")
print("Nombre completo:", nombre_completo)
print("Edad: ", edad, "años")
print("Estatura:", estatura, "cm")
print("Peso:", peso, "Kg")
print("Dirección:", direccion)
print("Número Telefónico:", numero_telefonico)
