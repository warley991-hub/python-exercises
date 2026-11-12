def apply(criteria, n):
    '''
    criteria: uma função que pega um número e retorna um valor booleano
    n: um número inteiro 
    Retorna quantos números de 0 até n (inclusivo) batem com criteria
    '''

    count = 0
    for i in range(n+1):
        if criteria(i):
            count += 1
    return count

def is_even(x):
    return x%2==0

print(apply(is_even, 600))