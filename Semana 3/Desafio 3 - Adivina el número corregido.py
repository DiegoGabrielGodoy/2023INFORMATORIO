import random

#Pedir al usuario que ingrese su nombre.
nombre = input("Por favor ingrese un nombre de usuario: ")

#Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
print("Hola", nombre, "el día de hoy tendrás que adivinar un número entre el 1 y el 100, solo tienes 8 intentos para adivinarlo, ¿Estás listo? Vamos a jugar")

#Generar aleatoriamente un número entero entre 1 y 100.
numero_aleatorio = random.randint(1, 100)
intentos = 8

while intentos > 0:
    #Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
    print("Te quedan", intentos, "intentos.")
    numero_intento = input("Introduce tu intento para comenzar a jugar: ")

    #El "número" ingresado por el usuario puede:
    #No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
    if not numero_intento.isdigit():
        print("El número que usted ingresó, no corresponde a un número entero")
        continue

    #Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento lo adivinó.
    if int(numero_intento) == numero_aleatorio:
        print("¡Felicidades! Adivinaste el número aleatorio en el intento", 9 - intentos)
        break

    #Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
    elif int(numero_intento) > numero_aleatorio:
        print("El número es menor que", numero_intento)

    #Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
    else:
        print("El número es mayor que", numero_intento)

    intentos -= 1

#Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el número que tenía que adivinar.
if intentos == 0:
    print("Lo siento, te quedaste sin intentos. El número aleatorio era", numero_aleatorio)