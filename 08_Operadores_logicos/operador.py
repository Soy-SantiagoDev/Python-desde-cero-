# =====================================
# Operador Lógico NOT
# =====================================
# El operador lógico NOT invierte
# el resultado de una condición.
#
# Si la condición es verdadera,
# NOT la convierte en falsa.
#
# Si la condición es falsa,
# NOT la convierte en verdadera.
# =====================================

# Preguntar si el usuario está bloqueado.

bloqueo = input("¿El usuario está bloqueado? (si/no): ")

# Verificar que el usuario NO esté bloqueado.

if not bloqueo.lower() == "si":
    print("Tienes acceso.")
else:
    print("No tienes acceso.")
