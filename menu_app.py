# Función para agregar una compra a la lista
def agregar_compra(compras, total_gastado):
    try:
        compra = float(input("Ingrese el monto de la compra: "))  # Añadir manejo de excepciones para números no válidos
        compras.append(compra)
        total_gastado += compra
        print(f"Compra de ${compra} agregada correctamente.")
        return total_gastado
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido.")

# Función para mostrar las compras realizadas
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(compras, 1):
            print(f"Compra {i}: ${compra}")

# Función para mostrar el total gastado
def mostrar_total(total_gastado):
    print(f"El total gastado hasta ahora es: ${total_gastado}")  # Añadir un mensaje más claro

# Función para salir del programa
def salir():
    print("Hasta luego")
    exit()

# Función principal
def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == '2':
            mostrar_compras(compras)
        elif opcion == '3':
            mostrar_total(total_gastado)
        elif opcion == '4':
            salir()
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()