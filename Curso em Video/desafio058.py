import random
numeros = [0,1,2,3,4,5,6,7,8,9,10]
numero = random.choice(numeros)
tentativas = 1

while True:
    user_guess = int(input('Diga-me um número de 0 a 10: '))
    if user_guess == numero:
        print(f'Você acertou!\nO número de tentativas foi: {tentativas}')
        break
    else:
        print('Você errou!')
        tentativas+=1
        continue
