import random
numeros = [0,1,2,3,4,5]
numero = random.choice(numeros)

user_guess = int(input('Diga-me um número de 0 a 5: '))
if user_guess == numero:
    print('Você acertou!')
else:
    print('Você errou!')

