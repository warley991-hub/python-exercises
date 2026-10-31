'''
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!

def double_char(s):
    pass
'''

# def double_char(s):
#     s2x = ''
#     for char in s:
#         s2x += (char*2)
#     return s2x

def double_char(s):
    return ''.join([char*2 for char in s])

print(double_char("String"))