reta_a = float(input('Digite o comprimento da primeira reta: '))
reta_b = float(input('Digite o comprimento da segunda reta: '))
reta_c = float(input('Digite o comprimento da terceira reta: '))

if (reta_a + reta_b > reta_c) and (reta_a + reta_c > reta_b) and (reta_b + reta_c > reta_a):
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')