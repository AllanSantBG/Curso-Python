from pack import moeda


preco = float(input('Preço: R$'))
print(f'O preço aumentado em 10% é R${moeda.aumentar(valor=preco, porcentagem=10)}')
print(f'O preço reduzido em 20% é R${moeda.diminuir(valor=preco, porcentagem=20)}')
print(f'O preço dobrado é R${moeda.dobro(valor=preco)}')
print(f'O preço pela metade é R${moeda.metade(valor=preco)}')