class Inmueble:
    def __init__(self, antiguedad, metros, habitaciones, garaje, zona, estado):
        self.antiguedad = antiguedad
        self.metros = metros
        self.habitaciones = habitaciones
        self.garaje = garaje
        self.zona = zona
        self.precio = self.calcular_precio()
        self.estado = estado

    def calcular_precio(self):
        if self.zona == "A":
            return (self.metros * 100 + self.habitaciones * 500 + self.garaje * 1500) * (1 - (2023 - self.antiguedad) / 100)
        elif self.zona == "B":
            return ((self.metros * 100 + self.habitaciones * 500 + self.garaje * 1500) * (1 - (2023 - self.antiguedad) / 100) * 1.5)
        elif self.zona == "C":
            return ((self.metros * 100 + self.habitaciones * 500 + self.garaje * 1500) * (1 - (2023 - self.antiguedad) / 100) * 2)
        else:
            return 0
        
def calcular_precio(inmueble):
    precio_base = (inmueble['metros'] * 100) + (inmueble['habitaciones'] * 500) + (inmueble['garaje'] * 1500)
    antiguedad = 2023 - inmueble['año']

    if inmueble['zona'] == 'A':
        precio = precio_base * (1 - antiguedad / 100)
    elif inmueble['zona'] == 'B':
        precio = precio_base * (1 - antiguedad / 100) * 1.5
    elif inmueble['zona'] == 'C':
        precio = precio_base * (1 - antiguedad / 100) * 2
    return precio

# Formato de lista
inmuebles = [
    {'antigüedad': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'antigüedad': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'antigüedad': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'antigüedad': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'antigüedad': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]

# Agregar inmuebles a la lista
def agregar_inmueble():
    antiguedad = int(input("Ingrese la antigüedad del inmueble: "))
    metros = int(input("Ingrese los metros cuadrados del inmueble: "))
    habitaciones = int(input("Ingrese la cantidad de habitaciones del inmueble: "))
    garaje = input("¿Tiene garaje? (Sí/No): ").lower() == "sí"
    zona = input("Ingrese la zona del inmueble (A, B, C): ").upper()
    estado = "Disponible"
    inmueble = Inmueble(antiguedad, metros, habitaciones, garaje, zona, estado)
    inmueble_dict = {
        'antigüedad': inmueble.antiguedad,
        'metros': inmueble.metros,
        'habitaciones': inmueble.habitaciones,
        'garaje': inmueble.garaje,
        'zona': inmueble.zona,
        'precio': inmueble.precio,  # Agregar el precio calculado al diccionario
        'estado': inmueble.estado
    }

    if validar_inmueble(inmueble_dict):
        inmuebles.append(inmueble_dict)
        print("El inmueble ha sido agregado exitosamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

# Función para eliminar un inmueble de la lista
def eliminar_inmueble():
    mostrar_inmuebles()
    index = int(input("Ingrese el índice del inmueble a eliminar: "))
    if 0 <= index < len(inmuebles):
        inmueble = inmuebles[index]
        inmuebles.remove(inmueble)
        print("El inmueble ha sido eliminado exitosamente.")
    else:
        print("El índice del inmueble es inválido.")

# Función para validar un inmueble
def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['antigüedad'] <= 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    return True

# Función para mostrar los inmuebles
def mostrar_inmuebles():
    print("Lista de inmuebles:")
    for i, inmueble in enumerate(inmuebles):
        print(f"Inmueble {i}:")
        print(f"Antigüedad: {inmueble['antigüedad']}")
        print(f"Metros: {inmueble['metros']}")
        print(f"Habitaciones: {inmueble['habitaciones']}")
        print(f"Garaje: {'Sí' if inmueble['garaje'] else 'No'}")
        print(f"Zona: {inmueble['zona']}")
        print(f"Estado: {inmueble['estado']}")
        print("-----------")

# Función para editar el estado de un inmueble en la lista
def editar_estado():
    mostrar_inmuebles()
    index = int(input("Ingrese el índice del inmueble a editar: "))
    if 0 <= index < len(inmuebles):
        nuevo_estado = input("Ingrese el nuevo estado del inmueble (Disponible, Reservado, Vendido): ")
        inmuebles[index]['estado'] = nuevo_estado
        print("El estado del inmueble ha sido actualizado exitosamente.")
    else:
        print("El índice del inmueble es inválido.")

# Función para realizar una búsqueda de inmuebles según un presupuesto dado
def buscar_inmuebles(lista, presupuesto):
    inmuebles_encontrados = []

    for inmueble in lista:
        if inmueble['estado'] in ['Disponible', 'Reservado'] and Inmueble(inmueble['antigüedad'], inmueble['metros'], inmueble['habitaciones'], inmueble['garaje'], inmueble['zona'], inmueble['estado']).calcular_precio() <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = Inmueble(inmueble['antigüedad'], inmueble['metros'], inmueble['habitaciones'], inmueble['garaje'], inmueble['zona'], inmueble['estado']).calcular_precio()
            inmuebles_encontrados.append(inmueble_con_precio)

    return inmuebles_encontrados
# Función principal del programa
def main():
    while True:
        print("Bienvenido a la Inmobiliaria")
        print("1. Agregar inmueble")
        print("2. Editar estado de un inmueble")
        print("3. Eliminar inmueble")
        print("4. Buscar inmuebles según presupuesto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_inmueble()
        elif opcion == "2":
            editar_estado()
        elif opcion == "3":
            eliminar_inmueble()
        elif opcion == "4":
            presupuesto = float(input("Ingrese el presupuesto máximo: "))
            inmuebles_encontrados = buscar_inmuebles(inmuebles, presupuesto)
            if len(inmuebles_encontrados) == 0:
                print("No se encontraron inmuebles que cumplan con los requisitos.")
            else:
                print("Inmuebles encontrados:")
                for inmueble in inmuebles_encontrados:
                    print(inmueble)
        elif opcion == "5":
            print("¡Gracias por utilizar la Inmobiliaria!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()