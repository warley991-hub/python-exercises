def count_matches(d):
    """ d is a dict
    Returns how many entries in d have the key equal to its value """
    # equal = 0
    # for key,value in d.items():
    #     if key == value:
    #         equal += 1

    return sum(1 for key,value in d.items() if key == value)


# for example
d = {1:2, 3:4, 5:6}
print(count_matches(d))   # prints 0
d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # prints 2