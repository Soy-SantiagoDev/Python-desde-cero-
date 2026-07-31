# =====================================
# SOLUCIONES
# Condicional ELIF
# =====================================

# Solución 1

nota = int(input("Calificación: "))

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# Solución 2

edad = int(input("Edad: "))

if edad >= 60:
    print("Adulto mayor")
elif edad >= 18:
    print("Adulto")
else:
    print("Menor de edad")

# Solución 3

temperatura = int(input("Temperatura: "))

if temperatura >= 35:
    print("Hace mucho calor")
elif temperatura >= 20:
    print("Clima agradable")
else:
    print("Hace frío")

# Solución 4

numero = int(input("Número: "))

if numero > 0:
    print("Positivo")
elif numero == 0:
    print("Es cero")
else:
    print("Negativo")

# Solución 5

puntaje = int(input("Puntaje: "))

if puntaje >= 100:
    print("Nivel experto")
elif puntaje >= 50:
    print("Nivel intermedio")
else:
    print("Nivel principiante")