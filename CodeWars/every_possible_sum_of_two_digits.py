'''
Description:
Given a number >= 10, return all the possible sum of two digits of it.

In the output, the pairs of digits should be ordered first left-to-right for the first digit, then left-to-right for the second digit also.

For example, 12345: all possible sum of two digits from that number are:

[ 1 + 2, 1 + 3, 1 + 4, 1 + 5, 2 + 3, 2 + 4, 2 + 5, 3 + 4, 3 + 5, 4 + 5 ]

Therefore the result must be:

[ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]

def digits(num):
    pass
'''

def digits(num):
    sum_list = []
    num = str(num)

    for i in range(len(num) - 1):
        
        j = i + 1 
        
        while j < len(num):
            
            soma = int(num[i]) + int(num[j])
            sum_list.append(soma)
            
            j += 1
            
    return sum_list