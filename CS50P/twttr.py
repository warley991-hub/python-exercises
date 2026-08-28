user_input = str(input('Input: '))
user_input = str(user_input)
vowels = ['A','E','I','O','U','a','e','i','o','u']

for letter in user_input:
    if letter in vowels:
        user_input = user_input.replace(letter,'')
print(user_input)