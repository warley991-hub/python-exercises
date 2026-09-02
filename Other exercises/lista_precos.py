lista_produtos = [100,200,300,400,500,600]
reajuste = 0.05
nova_lista = []

for preco in lista_produtos:
    preco = preco * (1+reajuste)
    nova_lista.append(preco)
print(nova_lista)