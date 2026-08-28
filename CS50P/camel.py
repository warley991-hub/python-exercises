def camel_to_snake(input):
    for letter in input:
        if letter.isupper():
            x = letter
            input = input.replace(x, '_'+x)
    input = input.lower()
    print(f'snake_case: {input}')
    return f'snake_case: {input}'

def main():
    user_input = input('camelCase: ')
    camel_to_snake(user_input)
main()
