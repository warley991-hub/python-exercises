while True:
    try:
        n = int(input('Digite um número para ver a tabuada dele: '))
    except ValueError:
        print('Digite apenas números inteiros.')
        continue
    if n < 0:
        print(f'{"="*25}\nPROJETO FINALIZADO\n{"="*25}')
        break
    print(f'''{'='*25}
{'\n'.join([(f'{n} x {i} = {n*i}') for i in range(1,11)])}
{'='*25}''')