from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), 
        randint(0, 10), randint(0, 10))
maior = menor = numeros[0]
print(f'Números sorteados: ', end='')
for num in numeros:
    print(num, end=' ')
print(f'\nO maior valor é {max(numeros)}\nO menor valor é {min(numeros)}')