matriz = list()
numeros = list()
for linhas in range(1, 4):
    for colunas in range(1, 4):
        numeros.append(int(input(f'Digite o número na posição [{linhas}, {colunas}]: ')))
    matriz.append(numeros[:])
    numeros.clear()
for i in matriz:
    print(f'| {i[0]:^5} {i[1]:^5} {i[2]:^5} |')