'''
Escreva uma função que retorne uma tupla, o primeiro elemento deve
ser o número de vogais e o segundo elemento o número de consoantes
'''

def char_counts(s):
    '''
    s: uma string de caracters minúsculos
    '''
    vowels = 'aeiou'
    vowels_count = 0
    consonants = 0
    
    for char in s.lower():
        if char in vowels:
            vowels_count += 1
        elif char == ' ':
            pass
        else:
            consonants += 1

    return (vowels_count, consonants)

print(char_counts('Breno Warley'))