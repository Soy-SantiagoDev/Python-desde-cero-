# =====================================
# Instrucción CONTINUE
# =====================================
# La instrucción continue permite
# omitir una iteración del ciclo.
#
# Cuando Python encuentra continue,
# pasa inmediatamente a la siguiente
# repetición.
# =====================================

# Crear un contador.

contador = 0

# Repetir mientras el contador
# sea menor que 5.

while contador < 5:

    # Aumentar el contador.

    contador += 1

    # Omitir la repetición cuando
    # el contador sea igual a 3.

    if contador == 3:
        continue

    # Mostrar el número de repetición.

    print(f"Repetición número {contador}")
