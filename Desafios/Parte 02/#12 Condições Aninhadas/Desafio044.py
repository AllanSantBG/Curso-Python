preco = float(input('Digite o PREÇO do PRODUTO: R$'))
pagamento = int(input("""FORMA DE PAGAMENTO
|(1) À vista Dinheiro/Cheque
|(2) À vista Cartão
|(3) 2x Cartão
|(4) 3x ou mais Cartão
Digite a opção: """))
if pagamento == 1:
    total = preco - (preco * (10 / 100))
    parcelamento = 1
    info = 'com DESCONTO de 10%'
elif pagamento == 2:
    total = preco - (preco * (5 / 100))
    parcelamento = 1
    info = 'com DESCONTO de 5%'
elif pagamento == 3:
    total = preco
    parcelamento = 2
    info = ''
elif pagamento == 4:
    total = preco + (preco * (20 / 100))
    parcelamento = int(input('Digite o NÚMERO de VEZES em que irá DIVIDIR: '))
    info = 'com JUROS de 20%'
else:
    total = 0
    parcelamento = 1
    info = ''
    print('\033[7;30;41' + 'OPÇÃO INVALÍDA, TENTE NOVAMENTE' + '\033[m')
print(f'-O produto custa R${preco:.2f}', info, f'\n-O valor total da sua compra é R${total:.2f}\n-Parcelamento em {parcelamento}x de R${total / parcelamento:.2f}')