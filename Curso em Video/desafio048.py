soma = 0
for i in range(1,501):
    if i % 2 == 1:
        if i % 3 == 0:
            soma += i
print(f'''
============================================================
Soma total dos números ímpares entre 1 e 500 que são múltiplos de 3:
{soma:,}
============================================================
''')