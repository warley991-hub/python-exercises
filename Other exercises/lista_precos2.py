lista_produtos = [500, 9000, 900]
reajuste_5 = 0.05
reajuste_10 = 0.1
corte_faixa = 5000

lista_reajustada = []

for preco in lista_produtos:
    if preco > corte_faixa:
        preco = preco * (1+reajuste_5)
    else:
        preco = preco * (1+reajuste_10)
    lista_reajustada.append(preco)
print(lista_reajustada)