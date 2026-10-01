while True:
    genero = input('Digite o seu gênero (M/F): ').upper()

    if genero != 'M' and genero != 'F':
        print('Digite apenas \'M\' ou \'F\'')
        continue
    else:
        break