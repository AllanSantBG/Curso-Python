num = int(input('Digite um número inteiro: '))
i = 0
fat = 1
print('Número:', num)
print(f'{num}! = ', end='')
for i in range(0, num):
    i += 1
    fat = fat * i
    if i != num:
        print(f'{i} x', end=' ')
print(f'{i} = {fat}')