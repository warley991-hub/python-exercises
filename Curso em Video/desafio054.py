import datetime

ano_atual = datetime.datetime.now().year
maior_idade = 0

for i in range(7):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    if ano_atual - ano_nasc >= 21:
        maior_idade += 1

print(f"Quantidade de pessoas maiores de idade: {maior_idade}")