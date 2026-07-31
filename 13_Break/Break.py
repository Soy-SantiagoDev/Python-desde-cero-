# =====================================
# Instrucción BREAK
# =====================================
# La instrucción break permite salir
# inmediatamente de un ciclo.
#
# Cuando Python encuentra break,
# el ciclo termina.
# =====================================

# Repetir el ciclo indefinidamente.

while True:

    # Solicitar una palabra.

    palabra = input("Escribe la palabra salir para terminar: ")

    # Verificar si el usuario desea salir.

    if palabra == "salir":
        print("Programa finalizado.")
        break

    # Mostrar la palabra ingresada.

    print("Escribiste la palabra:", palabra)
