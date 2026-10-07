primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro

print("Os 10 primeiros termos são:")
contador = 10

while True:
    for i in range(contador):
        print(termo_atual)
        termo_atual += razao
    
    resposta = int(input('Mostrar mais quantos termos? [Digite 0 para fechar] '))
    if resposta != 0:
        contador = resposta
    else:
        print('Programa finalizado!')
        break

# for i in range(10):
#     print(termo_atual)
#     termo_atual += razao

# print("FIM")