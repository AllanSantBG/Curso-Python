cont = soma = maioresMil = 0
while True:
    cont += 1
    nome = str(input(f'Digite o nome do {cont}º produto: ').strip().title())
    preco = float(input(f'Digite o preço do {cont}º produto: R$'))
    soma += preco
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar (S/N): ').strip().upper()[0])
    print('=' * 30)
    if preco > 1000:
        maioresMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomeBarato = nome
    if resposta in 'N':
        break
print(f"""Dos {cont} produtos registrados
1. O total a ser gasto com os produtos é de R${soma:.2f}
2. {maioresMil} produtos tem o preço maior que R$1000,00
3. O produto {nomeBarato} é o mais barato, custando R${menor:.2f}""")