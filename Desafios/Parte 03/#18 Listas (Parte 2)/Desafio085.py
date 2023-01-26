numeros = [[], []]
for i in range(1, 8):
    num = float(input(f'{i}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Números pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')