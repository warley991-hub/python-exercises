from datetime import date

def main():
    while True:
        try:
            ano_nascimento = int(input('Digite o ano de nascimento: '))
            break
        except ValueError:
            print('Por favor, digite um ano válido (número inteiro).')

    verificar_alistamento(ano_nascimento)


def verificar_alistamento(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        ano_alistamento = ano_atual + saldo
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        print(f'Seu alistamento será em {ano_alistamento}.')
    else:
        saldo = idade - 18
        ano_alistamento = ano_atual - saldo
        print(f'Você já deveria ter se alistado há {saldo} anos.')
        print(f'Seu alistamento foi em {ano_alistamento}.')


if __name__ == "__main__":
    main()