import random
import time


opcoes = ['Pedra','Papel','Tesoura']


while True:
    try:
        escolha_usuario = int(input('''
==================
ESCOLHA UMA OPÇÃO:

[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
==================
Digite sua escolha: '''))
        if escolha_usuario <= 0 or escolha_usuario > 3:
                print('''
=================================           
Digite somente um número de 1 a 3.
=================================''')
                continue
        break
    except ValueError:
        print('''
=================================           
Digite somente um número de 1 a 3.
=================================''')


time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!')
time.sleep(0.5)


escolha_usuario = opcoes[escolha_usuario-1]
escolha_computador = random.choice(opcoes)


if escolha_usuario == 'Pedra' and escolha_computador == 'Papel':
     resposta = 'Você perdeu!'
elif escolha_usuario == 'Pedra' and escolha_computador == 'Tesoura':
     resposta = 'Você venceu!'
elif escolha_usuario == 'Papel' and escolha_computador == 'Pedra':
     resposta = 'Você venceu!'
elif escolha_usuario == 'Papel' and escolha_computador == 'Tesoura':
     resposta = 'Você perdeu!'
elif escolha_usuario == 'Tesoura' and escolha_computador == 'Pedra':
     resposta = 'Você perdeu!'
elif escolha_usuario == 'Tesoura' and escolha_computador == 'Papel':
     resposta = 'Você venceu!'
else:
     resposta = 'Vocês empataram!'


print(f'''
=================================
Você escolheu: {escolha_usuario}
O computador escolheu: {escolha_computador}
=================================
{resposta}
=================================''')
