valor_casa = float(input('Qual o valor da casa? '))
salario_comprador = float(input('Qual o seu salário? '))
qts_anos_pagar = float(input('Em quantos anos irá pagar? '))

prestacao_mensal = valor_casa / (qts_anos_pagar*12)

if prestacao_mensal > (salario_comprador*0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')