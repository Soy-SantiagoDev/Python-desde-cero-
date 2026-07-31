# =====================================
# Condicional ELIF
# =====================================
# La estructura elif permite evaluar
# varias condiciones en un mismo programa.
#
# Python ejecutará únicamente el primer
# bloque cuya condición sea verdadera.
# =====================================

# Solicitar la calificación del estudiante.

nota = int(input("Ingresa tu calificación (0 - 100): "))

# Evaluar la calificación.

if nota >= 90:
    print("Excelente")

elif nota >= 70:
    print("Aprobado")

else:
    print("Reprobaste")
