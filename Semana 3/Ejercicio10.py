#Escribe un programa que pida al usuario una cadena de texto y 
#luego imprima la misma cadena pero con todas las vocales en mayúscula.
cadena = input("Ingrese una cadena de texto: ")

# Crear una cadena nueva con las vocales en mayúsculas
nueva_cadena = ""
for letra in cadena:
    if letra.lower() in "aeiou":
        nueva_cadena += letra.upper()
    else:
        nueva_cadena += letra

print("La cadena con las vocales en mayúsculas es:")
print(nueva_cadena)
