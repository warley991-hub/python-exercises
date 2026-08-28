answer = str(input('What is the answer to the great question of life?').strip().lower())
response = 'Yes'

def output():
    if answer == '42':
        print(response)
    elif answer == 'forty-two':
        print(response)
    elif answer == 'forty two':
        print(response)
    else:
        print('No')
output()
