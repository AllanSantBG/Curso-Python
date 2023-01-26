from pack import moeda
from pack import dado


preco = str(input('Preço: R$'))
moeda.resumo(dado.leiaDinheiro(preco), 50, 25)