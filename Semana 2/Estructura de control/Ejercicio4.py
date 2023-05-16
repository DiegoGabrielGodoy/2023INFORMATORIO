#Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla si está aprobado (5 o más) o no.
nota = int(input("Ingrese la nota del alumno, del 0 al 10: "))
if nota >= 5 and nota <=10:
    print("Aprobado")
elif nota < 5 and nota >=0:
    print("Desaprobado")
elif nota >= 11 and nota <= -1:
    print("Error")
