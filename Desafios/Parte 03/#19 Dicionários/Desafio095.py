temp = dict()
dados = list()
gol = list()
while True:
    temp['nome'] = str(input('Nome: ')).strip().title()
    temp['partidas'] = int(input('Partidas: '))
    for i in range(0, temp['partidas']):
        gol.append(int(input(f'Gols na {i + 1}ª partida: ')))
    temp['gols'] = gol[:]
    gol.clear()
    temp['total'] = 0
    for i in temp['gols']:
        temp['total'] += i
    dados.append(temp.copy())
    temp.clear()
    r = ' '
    if r not in 'SN':
        r = str(input('Continuar (S/N): ')).strip().upper()[0]
    if r in 'N':
        break
    print('=' * 50)
print(f'{"Nº":^} {"NOME"} {"GOLS"} {"TOTAL"}')
cont = 0
for i in dados:
    print(f'{cont} {i["nome"]} {i["gols"]} {i["total"]}')
    cont += 1
print('=' * 50)
cont = 0
while True:
    num = int(input('Número (999 = PARAR): '))
    print('=' * 50)
    if num == 999:
        print('Programa finalizado, volte sempre!')
        break
    else:
        print(f'O jogador {dados[num]["nome"]} jogou {dados[num]["partidas"]} partidas')
        for i in dados[num]['gols']:
            cont += 1
            print('-' * cont, end='>')
            print(f' {cont}ª partida fez {i} gols')
        print(f'Total de Gols nas partidas: {dados[num]["total"]}')
    print('=' * 50)