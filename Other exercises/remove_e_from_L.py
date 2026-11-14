'''
Write a function that meets the specification.   
Hint. Make a copy to save the elements. 
The use L.clear() to empty out the list and repopulate it with the ones you're keeping.  
'''

def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    Lcopy = L[:]

    L.clear()

    for element in Lcopy:
        if element == e:
            pass
        else:
            L.append(element)

L = [1, 2, 2, 2]
remove_all(L, 2)
print(L)      # prints [1]