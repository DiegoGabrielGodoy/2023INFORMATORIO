#Crea una función llamada es_bisiesto que tome un año como parámetro y
#devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
#es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.

def es_bisiesto(fecha):
    fecha = int(fecha)
    if fecha % 4 != 0:
        return "No es bisiesto"
    elif fecha % 4 == 0 and fecha % 100 != 0:
        return "Es bisiesto"
    elif fecha % 4 == 0 and fecha % 100 == 0 and fecha % 400 != 0:
        return "No es bisiesto"
    elif fecha % 4 == 0 and fecha % 100 == 0 and fecha % 400 == 0:
        return "Es bisiesto"
     
fecha = input("Ingrese un año en formato aaaa para conocer si ese año es bisiesto o no: ")
resultado = es_bisiesto(fecha)
print (resultado)