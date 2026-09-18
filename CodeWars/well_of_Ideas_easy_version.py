'''
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array for good ideas 'good' and bad ideas 'bad'. 
If there are one or two good ideas, return 'Publish!', if there are more than 2 return 
'I smell a series!'. 

If there are no good ideas, as is often the case, return 'Fail!'.

def well(x):
    #your code here
    return ''
'''

def well(x):
    
    good_count = x.count('good')
    
    if good_count > 2:
        return 'I smell a series!'
    elif 0 < good_count <= 2:
        return 'Publish!'
    else:
        return 'Fail!'