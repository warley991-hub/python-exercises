'''
Your task in this kata is to implement a function that calculates the sum of the integers inside a string. For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.

Note: only positive integers will be tested.

def sum_of_integers_in_string(s):
    pass
'''

def sum_of_integers_in_string(s):
    caracteres = [char if char.isdigit() else " " for char in s]
    string = "".join(caracteres)
    numeros = string.split()

    return sum(int(num) for num in numeros)

print(sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939."))