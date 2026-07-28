# =====================================
# SOLUCIONES
# Condicionales if y else
# =====================================

# Solución 1

edad = int(input("Edad: "))

if edad >= 18:
    print("Puede ingresar.")
else:
    print("Acceso denegado.")

# Solución 2

calificacion = int(input("Calificación: "))

if calificacion >= 60:
    print("Aprobaste.")
else:
    print("Reprobaste.")

# Solución 3

temperatura = int(input("Temperatura: "))

if temperatura > 30:
    print("Hace mucho calor.")
else:
    print("El clima es agradable.")

# Solución 4

saldo = int(input("Saldo: "))

if saldo > 0:
    print("Tienes dinero disponible.")
else:
    print("Saldo insuficiente.")