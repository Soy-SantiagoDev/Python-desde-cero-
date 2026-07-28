# =====================================
# Operador lógico AND
# =====================================
# El operador AND permite comprobar
# que dos condiciones sean verdaderas
# al mismo tiempo.
# =====================================

edad = int(input("¿Cuántos años tienes? "))

if edad >= 18 and edad <= 60:
    print("Puedes participar.")
else:
    print("No puedes participar.")
