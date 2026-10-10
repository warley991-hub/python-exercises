'''
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"

def get_middle(s):
    pass
'''

def get_middle(s):
    tamanho = len(s)
    meio = tamanho // 2
    
    if tamanho % 2 == 0:
        return s[meio - 1 : meio + 1]
    else:
        return s[meio]