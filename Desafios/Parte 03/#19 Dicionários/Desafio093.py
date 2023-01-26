dados = dict()
gol = list()
dados['nome'] = str(input('Nome: ')).strip().title()
dados['partidas'] = int(input('Partidas: '))
for i in range(0, dados['partidas']):
    gol.append(int(input(f'Gols na {i + 1}ª partida: ')))
dados['gols'] = gol
dados['total'] = 0
for i in dados['gols']:
    dados['total'] += i
print(f'{"=" * 80}\nO jogador {dados["nome"]} fez {dados["partidas"]} partidas')
cont = 0
for i in dados['gols']:
    cont += 1
    print('-' * cont, end='>')
    print(f' {cont}ª partida fez {i} gols')
print(f'Total de Gols nas partidas é igual a {dados["total"]}')