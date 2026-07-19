peso = float(input(" ingresa tu peso en kg:"))
altura = float(input("ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"\nTu imc es: {imc: .2f}")

if imc < 18.5:
    print("peso bajo")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobrepeso")
else:
    print("obesidad")