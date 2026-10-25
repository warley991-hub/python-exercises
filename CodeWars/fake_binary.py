'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    pass
'''

def fake_bin(x):
    resultado = ""
    for n in x:
        if int(n) < 5:
            resultado += '0'
        else:
            resultado += '1'
    return resultado