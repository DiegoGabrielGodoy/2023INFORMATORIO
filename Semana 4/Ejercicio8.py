#Crea una función llamada es_palindromo que tome una cadena de texto como parámetro y 
#devuelva es palindromo si es un palíndromo (es decir, si se lee igual
#de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso contrario.

def es_palindromo(cadena):
    if cadena == cadena[::-1]:
        return "Es palíndromo"
    else:
        return "No es palíndromo"

cadena = input("Ingrese una cadena de texto: ")
cadena_minuscula = cadena.lower()
print(es_palindromo(cadena_minuscula))