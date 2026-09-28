nomes = []
idades = []
generos = []

for i in range(4):
    nome = input(f'Digite o nome da {i + 1}° pessoa: ')
    nomes.append(nome)
    idade = int(input(f'Digite a idade da {i + 1}° pessoa: '))
    idades.append(idade)
    genero = input(f'Digite o gênero da {i + 1}° pessoa (M/F): ').strip().upper()
    generos.append(genero)

print(f"A média de idade do grupo é: {sum(idades) / len(idades):.2f} anos")
print(f"O homem mais velho é: {nomes[idades.index(max(idades))] if 'M' in generos else 'Nenhum homem informado'}")
print(f"O número de mulheres com menos de 20 anos é: {sum(1 for i in range(4) if generos[i] == 'F' and idades[i] < 20)}")