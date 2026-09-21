MIRIM = 9
INFANTIL = 14
JUNIOR = 19
SENIOR = 25

def main():
    try:
        ano_nasc = int(input('Informe o ano do seu nascimento: '))
    except ValueError:
        print('Digite somente números.')