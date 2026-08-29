num_1 = float(input('Digite o 1° número: '))
num_2 = float(input('Digite o 2° número: '))
num_3 = float(input('Digite o 3° número: '))
num_list = (num_1,num_2,num_3)
sorted_list = sorted(num_list,reverse=True)

print(f'O maior número é {sorted_list[0]} e o menor número é {sorted_list[2]}')