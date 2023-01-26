def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)')


n = str(input('Nome: ').strip())
g = str(input('Gols: ').strip())
if g.isnumeric() == True:
    if n.isalpha() == True:
        valor = ficha(nome=n, gols=g)
    else:
        valor = ficha(gols=g)
else:
    g = 0
    if n.isalpha() == True:
        valor = ficha(nome=n, gols=g)
    else:
        valor = ficha(gols=g)