x = 34
tentativas = 0

while True:
    user_input = int(input('Advinhe o valor de X: '))
    if user_input < x:
        print('Muito baixo!')
        tentativas += 1
    elif user_input > x:
        print('Muito alto!')
        tentativas += 1
    else:
        print(f'Você acertou! X = {x}')
        tentativas += 1
        print(f'Você acertou em {tentativas} tentativas.')
        break