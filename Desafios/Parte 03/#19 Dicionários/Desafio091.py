from random import randint
resultados = list()
dados = dict()
for i in range(0, 4):
    resultados.append(randint(1, 6))
    resultados.append(f'Jogador {i + 1}')
    dados[f'Jogada {i + 1}'] = resultados[:]
    print(f'Jogada {i + 1} tirou {resultados[0]}')
    resultados.clear()
print('=' * 20, f'\n{"RANKING":^20}')
cont = 0
sort = sorted(dados.values(), reverse=True)
for i in sort:
    cont += 1
    print(f'{cont}º: {i[1]} = {i[0]}')
print(f'O GANHADOR FOI {sort[0][1].upper()}!')