# =====================================
# Comparadores y Condiciones
# =====================================
# Los operadores de comparación permiten
# comparar dos valores.
#
# El resultado de una comparación puede
# ser True (Verdadero) o False (Falso).
# =====================================

# Operadores de comparación
#
# ==  Igual que
# !=  Diferente de
# >   Mayor que
# <   Menor que
# >=  Mayor o igual que
# <=  Menor o igual que

edad = int(input("¿Cuántos años tienes? "))

if edad == 18:
    print("Tienes exactamente 18 años.")
elif edad > 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

if edad != 18:
    print("No tienes exactamente 18 años.")
