#Crea una función llamada es_par que tome un número como parámetro y devuelva 
#Es par si el numero cumple con dichas condiciones y en caso contrario devuelva 
#Es impar o No es par.

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 7
if es_par(numero):
    print(f"{numero} es un número par")
else:
    print(f"{numero} es un número impar")