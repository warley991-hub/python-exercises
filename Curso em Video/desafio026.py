frase = input('Digite uma frase: ').upper()
print(frase)

a_count = frase.count('A')
first_pos = frase.find('A')
last_post = frase.rfind('A')

print(f'''A letra \'A\' aparece {a_count} vezes na frase.
A primeira aparição que a letra \'A\' aparece é na {first_pos}° posição.
A última aparição da letra \'A\' na frase é na {last_post}° posição.
''')