#Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad en años.
#Utiliza la función .split()
from datetime import date

fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ")
dia, mes, anio = fecha_nacimiento.split("/")
fecha_nacimiento = date(int(anio), int(mes), int(dia))
hoy = date.today()
edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

print("Tu edad es:", edad, "años")