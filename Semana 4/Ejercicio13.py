#Crea una función llamada calcular_descuento que tome dos parámetros precio y porcentaje_descuento. 
#La función debe calcular y devolver el precio después de aplicar el descuento.

def calcular_descuento(precio, porcentaje_descuento):
    if precio > 0:
        precio_total = precio - (precio * porcentaje_descuento)/100 
        return precio_total
    else: precio = 0
    return "No se puede aplicar descuento"

precio = int(input("Ingrese el valor del producto seleccionado: "))
porcentaje_descuento = int(input("Ingrese el porcentaje que desea aplicar: "))
precio_total = calcular_descuento(precio, porcentaje_descuento)

print(f"El precio total del producto es: {precio_total}")

