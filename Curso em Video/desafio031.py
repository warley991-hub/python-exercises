dist_viagem = float(input('Qual a distância da viagem? (KM)'))

if dist_viagem <= 200:
    preco = dist_viagem*0.5
    print(f'O preço da passagem ficará em {preco} R$')
else:
    preco = dist_viagem*0.45
    print(f'O preço da passagem ficará em {preco} R$')