numero = int(input('Digite um número: '))

print(f'==== TABUADA DO NÚMERO {numero} ====')

for i in range(11):
    print(f'''{i} * {numero} = {i*numero}''')
print('==========================')