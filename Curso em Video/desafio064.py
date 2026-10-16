qtde_digitado = 0
num_digitados = []

while True:
    try:
        n = int(input('''===== Digite um número inteiro - 999 PARA CANCELAR =====\n'''))
        qtde_digitado += 1
        num_digitados.append(n)
        soma = sum(num_digitados)-999

        if n == 999:
            print('PROGRAMA CANCELADO')
            print('A quantidade de números digitados foi de {} e a soma é de {}'.format(qtde_digitado-1, soma))
            break

    except ValueError:
        print('Digite somente números inteiros!\n')