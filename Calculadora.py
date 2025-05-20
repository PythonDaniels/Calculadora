while True:
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("❌ Ingrese solo números válidos.")

print("\n// Menú de operaciones //")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")
print("5 - Salir")

while True:
    try:
        opcion = int(input("\nSeleccione una opción (1-5): "))

        if opcion == 1:
            print(f"{numero1} + {numero2} = {numero1 + numero2}")
        elif opcion == 2:
            print(f"{numero1} - {numero2} = {numero1 - numero2}")
        elif opcion == 3:
            print(f"{numero1} * {numero2} = {numero1 * numero2}")
        elif opcion == 4:
            if numero2 == 0:
                print("❌ No se puede dividir entre cero.")
            else:
                print(f"{numero1} / {numero2} = {numero1 / numero2}")
        elif opcion == 5:
            print("👋 Saliendo de la calculadora...")
            break
        else:
            print("❌ Opción inválida. Elija un número del 1 al 5.")

    except ValueError:
        print("❌ Ingrese un número válido.")