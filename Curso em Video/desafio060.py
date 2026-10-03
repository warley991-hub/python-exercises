while True:
    try:
        numero = int(input('Digite um número inteiro: '))
        if numero <0:
            print('Digite somente números não negativos!')
        break
    except ValueError:
        print('Digite somente números inteiros!')

fatorial = numero
contador = numero

while contador > 1:
    fatorial = fatorial*(contador-1)
    contador -= 1

if numero == 0:
    print(f'O fatorial de {numero} é 1.')
else:
    print(f'O fatorial de {numero} é {fatorial}.')