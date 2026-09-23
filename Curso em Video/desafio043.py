peso = float(input("Digite o peso (kg): ").replace(',', '.'))
altura = float(input("Digite a altura (m): ").replace(',', '.'))

imc = peso / (altura ** 2)

print(f"IMC: {imc:.1f}")

if imc < 18.5:
    print("Status: Abaixo do Peso")
elif imc < 25:
    print("Status: Peso ideal")
elif imc < 30:
    print("Status: Sobrepeso")
elif imc < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade mórbida")