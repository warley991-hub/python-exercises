pesos = []

for i in range(5):
    peso = float(input(f'Informe o peso da {i + 1}ª pessoa (em kg): '))
    pesos.append(peso)

print(f"O maior peso informado foi: {max(pesos)} kg")
print(f"O menor peso informado foi: {min(pesos)} kg")