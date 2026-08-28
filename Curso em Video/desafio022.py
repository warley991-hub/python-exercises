nome = input('Digite seu nome: ')
nome_upper = nome.upper()
nome_lower = nome.lower()
nome_qtde = len(nome.replace(' ','').strip())
primeiro_nome = nome.split()
qtde_primeiro_nome = len(primeiro_nome[0])

print(f'''
1 - Nome com todas as letras maiúsculas:
{nome_upper}

2 - Nome com todas as letras minúsculas:
{nome_lower}

3 - Total de letras do nome completo:
{nome_qtde}

4 - Total de letras do primeiro nome:
{qtde_primeiro_nome}
''')
