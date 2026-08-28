import math
angulo = float(input('Digite um ângulo °: '))
angulo_radiano = math.radians(angulo)
cosseno = math.cos(angulo_radiano)
seno = math.sin(angulo_radiano)
tangente = math.tan(angulo_radiano)

print(f'O cosseno de {angulo:.2f}° é {cosseno:.2f} e o seno é {seno:.2f} e a tangente é {tangente:.2f}.')