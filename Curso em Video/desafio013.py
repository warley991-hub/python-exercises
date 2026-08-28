salario = float(input('Digite o valor do salário: '))
aumento = 0.15
novo_salario = salario+(salario*aumento)

print(f'O salário de {salario:.2f} R$ com aumento de {aumento*100:.0f}% ficará em {novo_salario:.2f} R$.')