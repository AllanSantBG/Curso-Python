from pack import moeda


preco = float(input('Preço: R$'))
print(f'O preço aumentado em 10% é R${moeda.aumentar(preco, 10, True)}')
print(f'O preço reduzido em 20% é R${moeda.diminuir(preco, 20, True)}')
print(f'O preço dobrado é R${moeda.dobro(preco, False)}')
print(f'O preço pela metade é R${moeda.metade(preco, False)}')