def main():
    try:
        user_input = int(input('Digite um número: '))
    except ValueError:
        print('Você deve digitar um número inteiro!')
        return
    conversao(user_input)


def conversao(num):
    try:
        base_conversao = int(input(
'''
================================
ESCOLHA UMA BASE DE CONVERSÃO:

1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL
0 - CANCELAR
================================
'''))

    except ValueError:
        print('Escolha uma base de conversão válida! 1,2 ou 3.')
        return
    if base_conversao == 0:
            print('''
================================
OPERAÇÃO CANCELADA PELO USUÁRIO!
================================
            ''')
            exit()
    elif base_conversao == 1:
        binario_func(num)
    elif base_conversao == 2:
        octal_func(num)
    elif base_conversao == 3:
        hexa_func(num)
    else:
        print('Opção inválida! Digite 1, 2 ou 3.')
def binario_func(num):
    binario = []
    num2 = num
    print()
    while True:
        resto_divisao = num % 2
        binario.append(resto_divisao)
        num = num//2
        if num == 0:
            binario.reverse()
            binario_formatado = ''.join(map(str,binario))
            print(f'O número {num2} convertido para Binário é: {binario_formatado}')
            print()
            break

def octal_func(num):
    octal = []
    num2 = num
    print()
    while True:
        resto_divisao = num % 8
        octal.append(resto_divisao)
        num = num//8
        if num == 0:
            octal.reverse()
            octal_formatado = ''.join(map(str,octal))
            print(f'O número {num2} convertido para Octal é: {octal_formatado}')
            print()
            break

def hexa_func(num):
    hexa = []
    num2 = num
    print()
    while True:
        resto_divisao = num % 16
        hexa.append(resto_divisao)
        num = num//16
        if num == 0:
            hexa.reverse()
            for i,item in enumerate(hexa):
                if item == 10:
                    hexa[i] = 'A'
                if item == 11:
                    hexa[i] = 'B'
                if item == 12:
                    hexa[i] = 'C'
                if item == 13:
                    hexa[i] = 'D'
                if item == 14:
                    hexa[i] = 'E'
                if item == 15:
                    hexa[i] = 'F'
            hexa_formatado = ''.join(map(str,hexa))
            print(f'O número {num2} convertido para Hexadecimal é: {hexa_formatado}')
            print()
            break

main()