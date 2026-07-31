# =====================================
# SOLUCIONES
# Operador lógico NOT
# =====================================

# Solución 1

puerta = input("¿La puerta está cerrada? (si/no): ")

if not puerta.lower() == "si":
    print("Puedes entrar.")

# Solución 2

computadora = input("¿La computadora está apagada? (si/no): ")

if not computadora.lower() == "si":
    print("La computadora está funcionando.")

# Solución 3

producto = input("¿El producto está agotado? (si/no): ")

if not producto.lower() == "si":
    print("Producto disponible.")

# Solución 4

usuario = input("¿El usuario está suspendido? (si/no): ")

if not usuario.lower() == "si":
    print("Puedes iniciar sesión.")

# Solución 5

archivo = input("¿El archivo está dañado? (si/no): ")

if not archivo.lower() == "si":
    print("Archivo listo para abrir.")