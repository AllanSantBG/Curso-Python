from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(1, 3)
print('-' * 29)
print("""    PEDRA  PAPEL  TESOURA   |
____________________________|
| ( 1 ) PEDRA
| ( 2 ) PAPEL
| ( 3 ) TESOURA""")
jogador = int(input('Faça sua jogada: '))
print('-' * 29)
sleep(1)
print('PEDRA!')
sleep(1)
print('PAPEL!')
sleep(1)
print('TESOURA!')
print('-' * 29)
print('Você escolheu', itens[jogador - 1])
print('Computador escolheu', itens[computador - 1])
print('-' * 29)
msgVitoria = '\033[7;30;42m' + 'PARABÉNS! Você venceu o jogo!' + '\033[m'
msgDerrota = '\033[7;30;41m' + 'QUE PENA! Você perdeu o jogo!' + '\033[m'
if jogador != computador:
    if jogador == 1:
        if computador == 3:
            print(msgVitoria)
        else:
            print(msgDerrota)
    elif jogador == 2:
        if computador == 1:
            print(msgVitoria)
        else:
            print(msgDerrota)
    else:
        if computador == 2:
            print(msgVitoria)
        else:
            print(msgDerrota)
else:
    print('\033[7;30;43m' + 'QUASE! Você empatou o jogo!' + '\033[m')
print('-' * 29)