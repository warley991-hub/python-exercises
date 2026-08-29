velocidade = int(input('Digite a velocidade do carro (km/h): '))
limite = 80

if velocidade > 80:
    multa = (velocidade - limite)*7
    print(f'Você foi multado em {multa} R$')