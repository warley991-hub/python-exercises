primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro

print("Os 10 primeiros termos são:")

for i in range(10):
    print(termo_atual)
    termo_atual += razao

print("FIM")