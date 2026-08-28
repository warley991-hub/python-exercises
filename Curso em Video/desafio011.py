largura = float(input('Digite a largura da parede (m): '))
altura = float(input('Digite a altura da parede (m): '))
area = largura * altura
tinta_cobre = 2
qtde_tinta = area/tinta_cobre

print(f'''Com a largura da parede de {largura:,.1f}m e a altura de {altura:,.1f}m, você precisará de {qtde_tinta:.0f} latas de tinta para pintar toda a parede.
Área total da parede: {area} m²''')