from time import sleep

def main():
    while True:
        a, b = input_usuario()

        while True:
            acao_menu = menu()
            if acao_menu == '4':
                break

            elif acao_menu =='5':
                print('''
=====================
OPERAÇÃO FINALIZADA!
=====================
Para reabrir o programa,
rode o comando:

'python desafio059.py'
======================
''')
                sleep(2)
                exit()

            else:
                resultado = processar(acao_menu, a, b)
                print(f'========================\nO resultado da operação é:\n{resultado}\n========================')
            sleep(2)


def input_usuario():
    while True:
        try:
            valor1 = int(input('Digite o primeiro número: '))
        except ValueError:
            print('Digite somente números inteiros!')
            continue
        break
    while True:
        try:
            valor2 = int(input('Digite o segundo número: '))
        except ValueError:
            print('Digite somente números inteiros!')
            continue
        break
    return valor1, valor2


def menu():
    opcoes = ['1','2','3','4','5']
    while True:
        escolha_usuario = input('''
===================
SELECIONE UMA OPÇÃO
===================
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
''')
        if escolha_usuario not in opcoes:
            print('Digite uma opção válida! [1-5]')
            continue
        else:
            return escolha_usuario


def processar(acao_menu, a, b):
    if acao_menu == '1':
        return a+b
    elif acao_menu == '2':
        return a*b
    else:
        return f'{a} é maior que {b}' if a>b else f'{b} é maior que {a}' if b>a else f'{a} e {b} são iguais.'

if __name__ == '__main__':
    main()