#Crea una función llamada calcular_mayor_diferencia que tome una lista de números como parámetro y 
#devuelva la mayor diferencia entre el numero mas alto y el numero mas bajo en la lista.

def calcular_mayor_diferencia(numero):
    lista_numero = numero.split()
    if len(lista_numero) > 0:
        sorted(lista_numero)
        lista_numero = [int(num) for num in lista_numero]
        ultimo = max(lista_numero)
        primero = min(lista_numero)
        total = (ultimo - primero)
        return (total)

numero = input("Ingrese una lista de números por espacios separados: ")
valor_total = calcular_mayor_diferencia(numero)
print(f"La mayor diferencia entre el número mas alto y el numero mas bajo es: {valor_total}")

        