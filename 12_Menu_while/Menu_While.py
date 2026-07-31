# =====================================
# Proyecto 2
# Menú Interactivo
# =====================================
# Este programa muestra un menú con
# diferentes opciones.
#
# El ciclo while mantiene el programa
# en ejecución hasta que el usuario
# decide salir.
# =====================================

# Variable para almacenar la opción elegida.

opcion = ""

# Repetir mientras la opción sea diferente de 3.

while opcion != "3":

    print("\n=== MENÚ ===")
    print("1. Saludo")
    print("2. Mostrar mensaje")
    print("3. Salir")

    # Solicitar una opción.

    opcion = input("Selecciona una opción: ")

    # Evaluar la opción elegida.

    if opcion == "1":
        print("¡Hola, bienvenido!")

    elif opcion == "2":
        print("Sigue practicando Python.")

    elif opcion == "3":
        print("Fin del programa.")

    else:
        print("Opción no válida.")
