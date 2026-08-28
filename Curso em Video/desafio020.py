import random
nome_1 = input('Digite o 1° nome: ')
nome_2 = input('Digite o 2° nome: ')
nome_3 = input('Digite o 3° nome: ')
nome_4 = input('Digite o 4° nome: ')

ordem_apresentacao = [nome_1, nome_2, nome_3, nome_4]
nome_escolhido = random.shuffle(ordem_apresentacao)

print(f'''
A ordem para apresentação dos trabalhos é:
{ordem_apresentacao}
''')