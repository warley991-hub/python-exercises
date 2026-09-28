numero_usuario = int(input('Digite um número inteiro: '))

total_divisores = 0

for i in range(1, numero_usuario + 1):
    if numero_usuario % i == 0:
        total_divisores += 1

if total_divisores == 2:
    print(f"O número {numero_usuario} é primo.")
else:
    print(f"O número {numero_usuario} não é primo.")
