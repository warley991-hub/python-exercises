'''
Implement String#digit? (in Java StringUtils.isDigit(String)), 
which should return true if given object is a single digit (0-9), false otherwise.

def is_digit(n):
    #your code here
'''

def is_digit(n):
    return n.isdigit() and len(n) == 1