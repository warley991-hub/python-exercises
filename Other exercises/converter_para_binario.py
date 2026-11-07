'''
Desafio: Conversor Decimal para Binário
Implemente uma função em Python chamada converter_para_binario() e retorne um número inteiro em sua representação em binário como uma string.

Regras e Restrições
Lógica Algorítmica: Construa a lógica utilizando divisões sucessivas por 2 (ou operadores bit a bit), sem recorrer à função embutida bin() ou formatadores prontos como f"{numero:b}".

Tipo de Retorno: O resultado deve ser retornado como texto (str), preservando a sequência exata de bits.

Caso de Borda: Lembre-se de tratar a entrada 0.

'''

def converter_para_binario():

    num = int(input('Digite um número de base 10: '))

    if num < 0:
        is_neg = True
        num = abs(num)
    else:
        is_neg = False

    if num == 0:
        return '0'

    binario = ''

    while num > 0:
        binario = str(num%2) + binario
        num = num//2
    if is_neg:
        binario = '-' + binario

    return binario

print(converter_para_binario())