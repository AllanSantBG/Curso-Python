times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 
        'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 
        'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 
        'Atlético-GO', 'Avái', 'Juventude')
print(f'Times do Brasileirão Série A: {times}')
print('-' * 100)
print(f'Os 5 primeiros times colocados: {times[:5]}')
print('-' * 100)
print(f'Os 4 últimos times colocados: {times[-4:]}')
print('-' * 100)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-' * 100)
print(f'O Botafogo está na {times.index("Botafogo") + 1}ª posição')
print('-' * 100)