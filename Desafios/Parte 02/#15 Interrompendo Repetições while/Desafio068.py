from random import randint
cont = 0
while True:
    numJog = int(input('Digite um valor: '))
    numComp = randint(0 , 10)
    parImpar = ' '
    while parImpar not in 'PpIi':
        parImpar = str(input('Digite P para par ou I para ímpar: ')).strip()[0]
    soma = numComp + numJog
    print('-' * 30)
    print(f'Você escolheu {numJog} e o Computador {numComp}')
    print('-' * 30)
    if soma % 2 == 0:
        print(f'A soma dos números é {soma} que é PAR')
        if parImpar in 'Pp':
            print('Você venceu')
            print('-' * 30)
        else:
            print('Computador venceu')
            break
    else:
        print(f'A soma dos números é {soma} que é ÍMPAR')
        if parImpar in 'Ii':
            print('Você venceu')
            print('-' * 30)
        else:
            print('Computador venceu')
            break
    cont += 1
print('-' * 30)
print(f'GAME OVER!\nVocê venceu o computador {cont} vez(es) consecutiva(s)!')