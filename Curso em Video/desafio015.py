qtde_km_percorridos = float(input('Qual a quantidade de KM percorridos? '))
qtde_dias_alugado = int(input('Qual a quantidade de dias que o carro foi alugado? '))
valor_total_diaria = 60*qtde_dias_alugado
valor_total_km_rodado = 0.15*qtde_km_percorridos
total_a_pagar = valor_total_diaria+valor_total_km_rodado
print(f'O valor total a ser pago pelo aluguel do carro é: R${total_a_pagar:.2f}')