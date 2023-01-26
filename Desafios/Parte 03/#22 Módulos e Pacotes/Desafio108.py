from pack import moeda


preco = float(input('Preço: R$'))
print(f'O preço aumentado em 10% é R${moeda.corrigir(moeda.aumentar(preco, 10))}')
print(f'O preço reduzido em 20% é R${moeda.corrigir(moeda.diminuir(preco, 20))}')
print(f'O preço dobrado é R${moeda.corrigir(moeda.dobro(preco))}')
print(f'O preço pela metade é R${moeda.corrigir(moeda.metade(preco))}')