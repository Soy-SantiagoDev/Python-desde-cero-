# =====================================
# SOLUCIONES
# Instrucción CONTINUE
# =====================================

# Solución 1

contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print(contador)

# Solución 2

contador = 0

while contador < 8:
    contador += 1

    if contador == 2:
        continue

    print(contador)

# Solución 3

while True:

    numero = int(input("Número: "))

    if numero == 0:
        continue

    print(numero)

# Solución 4

contador = 0

while contador < 15:
    contador += 1

    if contador == 10:
        continue

    print(contador)

# Solución 5

contador = 0

while contador < 20:
    contador += 1

    if contador == 7 or contador == 14:
        continue

    print(contador)