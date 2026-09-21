from datetime import date

MIRIM = 9
INFANTIL = 14
JUNIOR = 19
SENIOR = 25

def main():
    try:
        ano_nasc = int(input('Informe o ano do seu nascimento: '))
        ano_atual = date.today().year
        idade = ano_atual - ano_nasc
        
        print(f'O atleta tem {idade} anos.')
        
        if idade <= MIRIM:
            print('Classificação: MIRIM')
        elif idade <= INFANTIL:
            print('Classificação: INFANTIL')
        elif idade <= JUNIOR:
            print('Classificação: JÚNIOR')
        elif idade <= SENIOR:
            print('Classificação: SÊNIOR')
        else:
            print('Classificação: MASTER')

    except ValueError:
        print('Erro: Digite somente números inteiros válidos.')

if __name__ == '__main__':
    main()