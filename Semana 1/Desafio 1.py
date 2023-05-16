#Desafío 1:Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
#sus ventas totales y el departamento comercial te solicita que ayudes a los
#vendedores a calcular sus comisiones creando un programa que les pregunte su nombre y cuánto han vendido en éste mes.
#Tu programa le va a responder con una frase que incluya su nombre y el monto que le corresponde por las comisiones
nombre=str(input("Ingresa el nombre del empleado: "))
ventas=float(input("Ingresa, en pesos, la cantidad de ventas totales que realizo este mes: "))
comision=((ventas*6)/100)
print("El empleado", nombre,"le corresponde una comision del", comision, )