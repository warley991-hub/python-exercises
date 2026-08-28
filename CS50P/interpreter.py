expression = str(input('Expression: '))
expression_split = expression.split()
x = int(expression_split[0])
y = expression_split[1]
z = int(expression_split[2])

if y == '+':
    result = float(x + z)
elif y == '-':
    result = float(x - z)
elif y == '*':
    result = float(x * z)
elif y == '/':
    result = float(x / z)

print(result)
