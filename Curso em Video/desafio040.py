NOTA_REPROVADO = 5.0
NOTA_APROVADO = 7.0

def main():

    try:
        nota_1 = float(input('Digite sua primeira nota: '))
        nota_2 = float(input('Digite sua segunda nota: '))
        media = calcular_media(nota_1, nota_2)
        print(situacao_aluno(media))
    except ValueError:
        print('Digite somente números.')


def calcular_media(nota_1, nota_2):

    return (nota_1+nota_2)/2


def situacao_aluno(media):

    if media < NOTA_REPROVADO:
        situacao = f'Sua média foi: {media}, você foi REPROVADO!'
    elif NOTA_REPROVADO <= media < NOTA_APROVADO:
        situacao = f'Sua média é {media}, você está de RECUPERAÇÃO!'
    else:
        situacao = f'Sua média é {media}, você foi APROVADO!'
    return situacao


if __name__ == '__main__':
    main()