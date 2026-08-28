import math
com_cateto_oposto = int(input('Digite o comprimento do cateto oposto: '))
com_cateto_adjacente = int(input('Digite o comprimento do cateto adjacente: '))
hipotenusa_quadrado = pow(com_cateto_oposto,2) + pow(com_cateto_adjacente,2)
hipotenusa = print(f'A hipotenusa de {com_cateto_oposto}cm e {com_cateto_adjacente}cm é {math.sqrt(hipotenusa_quadrado)}')