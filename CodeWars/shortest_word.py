'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

def find_short(s):
    # your code here
    return l # l: shortest word length
'''

def find_short(s):
    l = s.split()

    len_words = []
    for word in l:
        len_words.append(len(word))

    return (min(len_words)) # l: shortest word length