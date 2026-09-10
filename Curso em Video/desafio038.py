def main():
    while True:
        try:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite o segundo número: '))
            comparacao(num1,num2)
        except ValueError:
            print('Digite um número inteiro.')
            continue
        break

def comparacao(n1,n2):
    if n1 > n2:
        print(f'O primeiro valor ({n1}) é o maior.')
    elif n1 < n2:
        print(f'O segundo valor ({n2}) é o maior.')
    else:
        print('Não existe valor maior, os dois são iguais.')

if __name__ == "__main__":
    main()