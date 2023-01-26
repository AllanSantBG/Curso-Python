produtosPrecos = 'farinha de trigo', 5, 'achocolatado em pó', 7, 'refrigerante 2L', 9, 'leite', 7, 'açúcar', 4
print('=' * 50)
print(f'{"LISTA DE PREÇOS":^50}')
print('=' * 50)
for pos in range(0, len(produtosPrecos), 2):
    print(f'{produtosPrecos[pos].title():.<40}R${produtosPrecos[pos + 1]:>8.2f}')
print('=' * 50)