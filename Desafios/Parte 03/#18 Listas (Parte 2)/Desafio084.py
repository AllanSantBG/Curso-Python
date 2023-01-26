pessoas = list()
dados = list()
resposta = 'S'
while resposta not in 'N':
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso(Kg): ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Continuar (S/N): ')).strip().upper()[0]
    if resposta not in 'SN':
        print('Resposta inválida, digite novamente')
    print('=' * 30)
print(f'Foram registradas {len(pessoas)} pessoas')
print(f'O maior peso registrado foi {maior}Kg, de ', end='')
for i in pessoas:
    print(i[0], end=' ') if i[1] == maior else dados.clear()
print(f'\nO menor peso registrado foi {menor}Kg, de ', end='')
for i in pessoas:
    print(i[0], end=' ') if i[1] == menor else dados.clear()