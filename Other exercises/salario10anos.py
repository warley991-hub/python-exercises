salario = 2000
aumento_por_ano = 0.1
tempo_total = 10

for i in range(tempo_total):
    salario = salario * (1 + aumento_por_ano)
print(salario)