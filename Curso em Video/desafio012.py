preco_produto = float(input('Digite o preço do produto: '))
desconto = 0.05
novo_preco = preco_produto-(preco_produto*desconto)
print(f'''O preço inicial do produto era de {preco_produto:.2f} R$
O preço com desconto de {desconto*100:.0f}% fica em {novo_preco:.2f} R$.''')