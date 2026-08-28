import random
nome_1 = input('Digite o 1° nome: ')
nome_2 = input('Digite o 2° nome: ')
nome_3 = input('Digite o 3° nome: ')
nome_4 = input('Digite o 4° nome: ')

lista_alunos = [nome_1, nome_2, nome_3, nome_4]
nome_escolhido = random.choice(lista_alunos)

print(f'O aluno sorteado para apagar o quadro foi: {nome_escolhido}')