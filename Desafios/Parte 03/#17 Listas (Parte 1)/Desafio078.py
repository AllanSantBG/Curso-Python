numeros = []
for i in range(1 , 6):
    num = float(input(f'Digite o {i}º número: '))
    numeros.append(num)
print(f'Números inseridos: {numeros}')
maior = max(numeros)
print(f'O menor número registrado foi {maior}, nas posições ', end='')
for i in range(0 , 5):
    if numeros[i] == maior:
        print(numeros.index(maior, i) + 1, end=' ')
print('')
menor = min(numeros)
print(f'O menor número registrado foi {menor}, nas posições ', end='')
for i in range(0 , 5):
    if numeros[i] == menor:
        print(numeros.index(menor, i) + 1, end=' ')