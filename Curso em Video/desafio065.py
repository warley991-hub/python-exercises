numeros_digitados = []

while True:
    try:
        n = int(input('Digite um número inteiro: '))
        numeros_digitados.append(n)
    except ValueError:
            print('Digite um valor inteiro!')
            continue

    while True:
        resposta = input('Deseja digitar mais valores? [S-N] ').strip().upper()
        if resposta in ['S','N']:
            break
        print('Resposta inválida! Tente novamente.')
    if resposta == 'N':
        print('Programa finalizado!')
        break

soma_numeros = sum(numeros_digitados)
media = soma_numeros/(len(numeros_digitados))
print(f'A lista de números digitados é: {numeros_digitados}')
print(f'A média entre todos os números é: {media}')
print(f'O maior número digitado foi {max(numeros_digitados)} e o menor número foi {min(numeros_digitados)}.')