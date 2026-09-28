soma = 0
for i in range(6):
    numero_usuario = int(input('Digite um número inteiro: '))
    if numero_usuario % 2 == 0:
        soma += numero_usuario

print(f'A somas dos números pares é: {soma}')