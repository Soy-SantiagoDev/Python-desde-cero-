opcion = ""

while opcion != "3":
    print("\n=== MENU ===")
    print("1. saludo")
    print("2. mostrar mensaje")
    print("3. salir")

    opcion = input("selecciona una opcion: ")

    if opcion == "1":
        print("hola, bienvenido")
    elif opcion == "2":
        print("sigue practicando python")
    elif opcion == "3":
        print("fin del programa")
    else:
        print("opcion no valida")
