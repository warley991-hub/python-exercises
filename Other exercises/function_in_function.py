def numero(a):
    def dobro(b):
        return a*b
    return dobro

a = numero(2)
resultado = a(3)

print(resultado)
