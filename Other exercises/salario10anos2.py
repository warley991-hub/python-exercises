salario= 2000
aumento_ano= 0.1
meta_salario= 10000
tempo_decorrido= 0

while salario < meta_salario:
    salario = salario * (1+aumento_ano)
    tempo_decorrido = tempo_decorrido+1
print (tempo_decorrido)