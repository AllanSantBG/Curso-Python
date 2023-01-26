from math import hypot
opposite = float(input('Digite o comprimento do Cateto Oposto: '))
adjacent = float(input('Digite o comprimento do Cateto Adjacente: '))
print(f'A hipotenusa do triangulo com catetos {opposite} e {adjacent} é igual a {hypot(opposite, adjacent):.2f}')