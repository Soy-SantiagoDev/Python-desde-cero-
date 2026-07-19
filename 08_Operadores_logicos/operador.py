bloqueo = input("¿El usuario está bloqueado? (si/no):")

if not bloqueo.lower() == "si":
    print("Tienes acceso")
else:
    print("No tienes acceso.")