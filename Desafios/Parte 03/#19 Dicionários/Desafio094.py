temp = dict()
dados = list()
media = 0
while True:
    temp['nome'] = str(input('Nome: ')).strip().title()
    temp['sexo'] = ' '
    while temp['sexo'] not in 'MF':
        temp['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
    temp['idade'] = int(input('Idade: '))
    media += temp['idade'] / 2
    dados.append(temp.copy())
    temp.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Continuar (S/N): ')).strip().upper()[0]
    if r in 'N':
        break
    print('-' * 50)
print(f'Foram registradas {len(dados)} pessoa(s)')
print(f'A média de idade é igual a {media}')
for v in dados:
    if v['sexo'] in 'F':
        print(f'Mulher: {v["nome"]}')
    if v['idade'] > media:
        print(f'Idade maior que a média: {v["nome"]}')