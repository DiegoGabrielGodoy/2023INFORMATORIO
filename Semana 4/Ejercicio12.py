#Crea una función llamada convertir_temperatura que tome una temperatura en grados Celsius y 
#la convierta a grados Fahrenheit. La fórmula de conversión es: Fahrenheit = (Celsius * 9/5) + 32.

def convertir_temperatura(celsius):
    if celsius.isdigit():
        celsius = int(celsius)
        Fahrenheit = (celsius * 9/5) + 32
        return Fahrenheit
    else:
        return "Error, el valor ingresadi no es un número válido"

celsius = input("Ingrese una temperatura en grados Celsius, para conocer los grados en Fahrenheit: ")
fahrenheint = convertir_temperatura(celsius)
print(f"Los grados en Fehrenheint son: {fahrenheint}")
