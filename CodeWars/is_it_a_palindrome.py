''''
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.

def is_palindrome(s):
    return

'''

# def is_palindrome(s):
#     s = list(s.lower())
#     x = s[:]
#     x.reverse()
#     return x == s

# print(is_palindrome('ABA'))

def is_palindrome(s):
    return list(s.lower()) == list(reversed(s.lower()))

print(is_palindrome('ABA'))