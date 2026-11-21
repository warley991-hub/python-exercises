# Write a recursive function that reverses a list of elements at the top-level only.
# Do NOT reverse elements inside nested lists.

def my_rev(L):
    """
    L is a non-empty list of elements (may contain nested lists).
    Returns a new list with the top-level elements of L in reverse order.
    """
    if len(L) == 1:
        return L
    else:
        return my_rev(L[1:]) + [L[0]]

print(my_rev([10, 20, 30, 40]))          # [40, 30, 20, 10]
print(my_rev([1, [2, 3], [4, 5, 6]]))    # [[4, 5, 6], [2, 3], 1]