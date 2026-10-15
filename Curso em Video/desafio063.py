n = int(input('Digite um número inteiro: '))

elementos = int(input('Digite quantos elementos deseja mostrar: '))

sequencia = [0,1]

while len(sequencia) < (n + elementos):
    soma = sequencia[-1] + sequencia[-2]
    sequencia.append(soma)

print(sequencia[n:n + elementos])