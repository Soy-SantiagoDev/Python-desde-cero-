# =====================================
# Operador lógico OR
# =====================================
# El operador OR permite que una de las
# condiciones sea verdadera para ejecutar
# el bloque de código.
# =====================================

experiencia = int(input("¿Cuántos años de experiencia tienes? "))
titulo = input("¿Tienes título? (sí o no): ").lower()

if experiencia >= 5 or titulo == "sí":
    print("Puedes aplicar.")
else:
    print("No puedes aplicar.")
