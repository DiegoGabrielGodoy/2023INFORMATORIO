#Escribe un programa que pida al usuario una cadena de texto y 
#determine cuántas veces aparece cada letra en la cadena.

print("Ingrese una cadena de texto, para saber cuantas veces aparece cada letra:")
cadena = input()
repeticion = {}
letra_may = cadena.upper()

for letra in letra_may:
    if letra != " " and letra.isalpha():
        if letra in repeticion:
            repeticion[letra] += 1
        else:
            repeticion[letra] = 1

print("La frecuencia que aparece cada letra es:")
for letra, repeticion in repeticion.items():
    print(f"La letra {letra} aparece {repeticion} veces")

