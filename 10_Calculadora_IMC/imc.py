# =====================================
# Proyecto 1
# Calculadora de Índice de Masa Corporal
# =====================================
# Este programa calcula el Índice de
# Masa Corporal (IMC) de una persona
# utilizando su peso y su altura.
# =====================================

# Solicitar el peso en kilogramos.

peso = float(input("Ingresa tu peso en kg: "))

# Solicitar la altura en metros.

altura = float(input("Ingresa tu altura en metros: "))

# Calcular el IMC.

imc = peso / (altura ** 2)

# Mostrar el resultado con dos decimales.

print(f"\nTu IMC es: {imc:.2f}")

# Clasificar el resultado.

if imc < 18.5:
    print("Peso bajo")

elif imc < 25:
    print("Peso normal")

elif imc < 30:
    print("Sobrepeso")

else:
    print("Obesidad")
