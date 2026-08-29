salario = float(input('Digite o valor do seu salário (R$): '))

if salario > 1250.0:
    aumento = 0.1
    novo_salario = salario+salario*aumento
    print(f'Seu novo salário com aumento é: {novo_salario}R$')
else:
    aumento = 0.15
    novo_salario = salario+salario*aumento
    print(f'Seu novo salário com aumento é: {novo_salario}R$')