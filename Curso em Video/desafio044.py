preco = float(input("Preço normal do produto: "))


print('''
Opções de Pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão
''')


opcao = int(input("Escolha a opção (1-4): "))


if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    print(f"Vai pagar em 2x de {total / 2:.2f}")
elif opcao == 4:
    total = preco + (preco * 0.20)
    parcelas = int(input("Quantas parcelas? "))
    print(f"Vai pagar em {parcelas}x de {total / parcelas:.2f} com juros")
else:
    total = 0
    print("Opção inválida. Tente novamente.")


if total > 0:
    print(f"Valor final a pagar: {total:.2f}")