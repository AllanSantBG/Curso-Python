numeros = []
for i in range(0, 5):
    num = float(input(f'Digite {i + 1}º número: '))
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(numeros):
            if num <= numeros[posicao]:
                numeros.insert(posicao, num)
                print(f'Adicionado a {posicao}ª posição')
                break
            posicao += 1
    print('-' * 40)
print(f'Números digitados em ordem: {numeros}')