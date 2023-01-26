preco = float(input('Digite o PREÇO do PRODUTO: R$'))
pagamento = int(input("""FORMA DE PAGAMENTO
|(1) Dinheiro/Cheque
|(2) Cartão
Digite a opção: """))
if pagamento == 1:
    porcentagem = preco * (10 / 100)
    print(f'-O produto que custa R${preco:.2f} tem desconto de 10% \n-O valor a ser cobrado é R${preco - porcentagem:.2f}')
else:
    parcelamento = int(input('Digite o NÚMERO de VEZES em que irá DIVIDIR(De 1 a 12): '))
    if parcelamento == 1:
        porcentagem = preco * (5 / 100)
        print(f'-O produto que custa R${preco:.2f} tem desconto de 5% \n-O valor a ser cobrado é R${preco - porcentagem:.2f}')
    elif parcelamento == 2:
        print(f'-O produto custa R${preco:.2f} \n-Dividido em parcelas de 2x de R${preco / 2:.2f}')
    else:
        porcentagem = preco * (20 / 100)
        print(f'-O produto que custa R${preco:.2f} tem juros de 20%\n-O valor total é de R${preco + porcentagem:.2f}, dividido em parcelas de {parcelamento}x de R${preco / parcelamento:.2f}')