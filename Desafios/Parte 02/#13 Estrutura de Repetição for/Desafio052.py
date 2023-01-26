num = int(input('Digite um NÚMERO INTEIRO: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[37m', end=' ')
        cont += 1
    else:
        print('\033[30m', end=' ')
    print(i, end=' ')
print('\033[m' + f'\nO número {num} é divisivel por {cont} número(s)')
if cont == 2:
    print('\033[m' + f'O número {num} é PRIMO')
else:
    print('\033[m' + f'O número {num} NÃO é PRIMO')