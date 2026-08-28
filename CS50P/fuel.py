def main():
    while True:
        fraction = str(input('Fraction: '))
        while not '/' in fraction:
            fraction = str(input('Fraction: '))
        else:
            try:
                fraction = fraction.split('/')
                x, y = fraction
                x = int(x)
                y = int(y)
            except ValueError:
                continue

        while (int(x) <0) or (int(y) <=0) or (x>y):
            fraction = input('Fraction: ')
            fraction = fraction.split('/')
            x, y = fraction
            x = int(x)
            y = int(y)

        result = percentage(x,y)
        if result <= 1:
            print('E')
        elif result  >= 99:
            print('F')
        else:
            print(f'{percentage(x,y)}%')
        break

def percentage(x,y):
    return round(float((x/y)*100))

main()
