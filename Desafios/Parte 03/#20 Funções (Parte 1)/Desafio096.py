def area(l, c):
    print(f'O terreno de dimensões {l}x{c} tem a área igual a {l * c}m²')

print('=' * 70)
print('CÁLCULO DE ÁREA DO TERRENO')
print('=' * 70)
larg = float(input('Largura do terreno: '))
comp = float(input('Comprimento do terreno: '))
area(larg, comp)
print('=' * 70)
