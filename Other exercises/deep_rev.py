# Write a recursive function that reverses a list of elements at ALL levels (deep reverse).
# If an element inside the list is itself a list, reverse it recursively as well.

def deep_rev(L):
    """
    L is a list of elements (may contain nested lists at any depth).
    Returns a new list with all elements of L and all nested lists reversed.
    """
    if len(L) == 0:
        return []
    elif type(L[0]) == list:
        return deep_rev(L[1:]) + [deep_rev(L[0])]
    else:
        return deep_rev(L[1:]) + [L[0]]

print(deep_rev([10, 20, 30, 40]))                  # [40, 30, 20, 10]
print(deep_rev([1, [2, 3], [4, [5, 6]]]))          # [[[6, 5], 4], [3, 2], 1]
print(deep_rev([[1, 2], [3, 4], [5, 6, 7]]))       # [[7, 6, 5], [4, 3], [2, 1]]