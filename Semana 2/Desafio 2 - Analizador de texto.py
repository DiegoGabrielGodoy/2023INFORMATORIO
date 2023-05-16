texto = input("Ingresa un artículo o una frase: ")
letra1 = input("Ingresa una letra a tu elección: ")
letra2 = input("Ingresa una segunda letra a tu elección: ")
letra3 = input("Ingresa una tercera letra a tu elección: ")

letras =[letra1.lower(), letra2.lower(), letra3.lower()]

# Convertir texto y letras a minúsculas
texto = texto.lower()

# 1- Contar las letras que se ingresaron
contador = {}
for letra in letras:
    contador[letra] = texto.count(letra.strip())

print("Cantidad de veces que aparecen las letras:")
for letra, cantidad in contador.items():
    print(f"{letra}: {cantidad}")

# 2- Contar las palabras en el texto
palabras = texto.split()
cantidad_palabras = len(palabras)
print(f"Hay {cantidad_palabras} palabras en el texto.")

# 3- Primera y última letra
texto_sin_espacios = texto.replace(" ", "")
primera_letra = texto_sin_espacios[0]
ultima_letra = texto_sin_espacios[-1]
print(f"La primera letra es {primera_letra} y la última letra es {ultima_letra}.")

# 4- Texto en orden inverso
texto_inverso = texto[::-1]
print("El texto en orden inverso es:")
print(texto_inverso)

# 5- Si "python" aparece en el texto
palabra_python = "python" in palabras
if palabra_python:
    print("La palabra 'Python' aparece en el texto.")
else:
    print("La palabra 'Python' no aparece en el texto.")
