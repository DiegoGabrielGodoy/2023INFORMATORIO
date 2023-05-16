#Vamos a crear un juego completamente funcional.
#Para ello el programa debe:
import random
# Pedir al usuario que ingrese su nombre.
nombre = input("Por favor ingrese un nombre de usuario: ")

#Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
print("Hola", nombre, "el día de hoy tendrás que adivinar un número entre el 1 y el 100, solo tienes 8 intentos para adivinarlo, ¿Estás listo? Vamos a jugar")

numero_aleatorio = random.randint(1, 100)
intentos = 8
#Generar aleatoriamente un número entero entre 1 y 100.
#tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)

while intentos > 0:
    intentos -= 1
    numero_intento = (input("Introduce tu intento para comenzar a jugar: "))
#El "número" ingresado por el usuario puede:
#No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
#tip 2: con el método isdigit() puedes saber si es posible convertir a entero    
    if not numero_intento.isdigit():
        print("El número que usted ingreso, no corresponde a un número entero")
        continue
#Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento lo adivinó.
    if numero_intento == numero_aleatorio:
        print("¡Felicidades! Adivinaste el número aleatorio, en el", intentos)
        break
    elif int(numero_intento) > numero_aleatorio:
#Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
        print("El número es menor que", numero_intento)
    else:
#Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
        print("El número es mayor que", numero_intento)
#En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que ingrese otro número.        
    if intentos > 0:
        print("Te quedan", intentos, "intentos.")
#Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el número que tenía que adivinar.
    else:
        print("Lo siento, te quedaste sin intentos. El número aleatorio era", numero_aleatorio)
