frase_usuario = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')

frase_invertida = frase_usuario[::-1]

if frase_usuario == frase_invertida:
    print(f"A frase '{frase_usuario}' é um palíndromo.")
else:
    print(f"A frase '{frase_usuario}' não é um palíndromo.")