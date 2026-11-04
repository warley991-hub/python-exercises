soma = 0
digitados = 0
while True:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n == 999:
        break
    soma += n
    digitados += 1
print(f'A soma dos {digitados} valores foi {soma}.')