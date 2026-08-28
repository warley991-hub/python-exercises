numero = input('Digite um número [0-9999]: ')
digitos = list(numero)
posicao = {
    'unidade': -1,
    'dezena': -2,
    'centena': -3,
    'milhar1': -4,
}

if len(digitos) == 1:
    print(f'Unidade: {digitos[posicao["unidade"]]}')
elif len(digitos) == 2:
    print(f'Unidade: {digitos[posicao["unidade"]]}')
    print(f'Dezena: {digitos[posicao["dezena"]]}')
elif len(digitos) == 3:
    print(f'Unidade: {digitos[posicao["unidade"]]}')
    print(f'Dezena: {digitos[posicao["dezena"]]}')
    print(f'Centena: {digitos[posicao["centena"]]}')
elif len(digitos) == 4:
    print(f'Unidade: {digitos[posicao["unidade"]]}')
    print(f'Dezena: {digitos[posicao["dezena"]]}')
    print(f'Centena: {digitos[posicao["centena"]]}')
    print(f'Milhar: {digitos[posicao["milhar1"]]}')
else:
    print('Digite um número de 0 até 9999')