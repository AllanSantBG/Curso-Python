matriz = list()
numeros = list()
somaPares = soma3Coluna = 0
maiores2Linha = list()
for linha in range(1, 4):
    for coluna in range(1, 4):
        num = int(input(f'Digite o número na posição [{linha}, {coluna}]: '))
        if num % 2 == 0:
            somaPares += num
        if coluna == 3:
            soma3Coluna += num
        if linha == 2:
            maiores2Linha.append(num)
        numeros.append(num)
    matriz.append(numeros[:])
    numeros.clear()
for i in matriz:
    print(f'| {i[0]:^5} {i[1]:^5} {i[2]:^5} |')
print(f'A soma dos valores pares é {somaPares}\nA soma dos valores da 3ª coluna é {soma3Coluna}\nO maior número da 2ª linha é {max(maiores2Linha)}')