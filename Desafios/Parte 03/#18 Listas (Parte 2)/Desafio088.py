from random import randint
jogos = list()
numeros = list()
quantidade = int(input('Digite a quantidade de jogos: '))
for i in range(quantidade):
    for l in range(0, 6):
        num = randint(1, 60)
        while num in numeros:
            num = randint(1, 60)
        numeros.append(num)
    jogos.append(numeros[:])
    numeros.clear()
    print(f'{i + 1}º Jogo: {jogos[i]}')