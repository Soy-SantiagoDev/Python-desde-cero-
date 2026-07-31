# =====================================
# SOLUCIONES
# Operador lógico OR
# =====================================

# Solución 1

edad = int(input("Edad: "))

if edad < 18 or edad > 60:
    print("Acceso permitido.")

# Solución 2

experiencia = int(input("Experiencia: "))
titulo = input("¿Tienes título? (Sí o No): ")

if experiencia >= 3 or titulo == "Si":
    print("Puedes participar.")

# Solución 3

temperatura = int(input("Temperatura: "))

if temperatura < 10 or temperatura > 35:
    print("Temperatura extrema.")

# Solución 4

calificacion = int(input("Calificación: "))

if calificacion == 100 or calificacion == 0:
    print("Calificación especial.")

# Solución 5

numero = int(input("Número: "))

if numero < 0 or numero > 100:
    print("Número fuera del rango.")