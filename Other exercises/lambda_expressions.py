preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 
                    'samsung galaxy': 3000, 'tv samsung': 1000, 
                    'ps5': 3000, 'tablet': 1000, 
                    'notebook dell': 3000, 'ipad': 3000, 
                    'tv philco': 800, 'notebook hp': 1700}


# Map - lambda
novos_precos1 = dict(map(lambda item: (item[0],item[1]*1.3), preco_tecnologia.items()))
print(f'\n ===== TESTE 1 ===== \n {novos_precos1}')


novos_precos2 = {produto: preco*1.3 for produto,preco in preco_tecnologia.items()}
print(f'\n ===== TESTE 2 =====\n {novos_precos2}')
for produto,preco in novos_precos2.items():
    print(f'\nProduto: {produto.title():<15} | Preço: {f"R$ {preco:.2f}":>10}', end='')


# Filter - Function
def eh_2000(item):
    return item[1]>2000


acima_2000 = list(filter(eh_2000, preco_tecnologia.items()))
for produto, preco in acima_2000:
    print(f'Produto: {produto.title():<15} | Preço: {f"R$ {preco:.2f}":>10}')


# Filter - lambda
acima_2000 = list(filter((lambda produto: produto[1]>2000), preco_tecnologia.items()))
print(acima_2000)


for produto, preco in acima_2000:
    print(f'Produto: {produto.title():<15} | Preço: {f"R$ {preco:.2f}":>10}')