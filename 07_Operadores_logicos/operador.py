# =====================================
# Operador Lógico OR
# =====================================
# El operador lógico OR permite comprobar
# dos o más condiciones.
#
# Si al menos una condición es verdadera,
# el resultado será verdadero.
# =====================================

# Solicitar los años de experiencia.
experiencia = int(input("¿Cuántos años de experiencia tienes? "))

# Solicitar si la persona tiene un título.
titulo = input("¿Tienes título? (Si o No): ")

# Verificar si la persona cumple alguno
# de los requisitos para aplicar.
#
# Puede aplicar si:
# - Tiene 5 años o más de experiencia.
# O
# - Tiene un título.

if experiencia >= 5 or titulo == "Si":
    print("Puedes aplicar.")
else:
    print("No puedes aplicar.")
