'''
Description:
Given a varying number of integer arguments, return the digits that are not present in any of them.

Example:

[12, 34, 56, 78]  =>  "09"
[2015, 8, 26]     =>  "3479"
Note: the digits in the resulting string should be sorted.

def unused_digits(*numbers):
    pass
    #your code here
'''

def unused_digits(*numbers):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    
    n_list = ''.join(str(n) for n in numbers)

    n_list = ''.join(d for d in digits if d not in n_list)
    return n_list

print(unused_digits(12, 34, 56, 78))