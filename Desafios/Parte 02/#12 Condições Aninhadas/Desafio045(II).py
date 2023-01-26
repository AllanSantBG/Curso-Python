from random import choice
from time import sleep
print('=' * 25)
print('=' * 25)
print('  PEDRA  PAPEL  TESOURA  ')
print('=' * 25)
print('=' * 25)
jogador = str(input('VAMOS JOGAR! \nDigite Pedra, Papel ou Tesoura: ')).strip().upper()
print(f'-VOCÊ escolheu {jogador}')
print('O COMPUTADOR ESTÁ JOGANDO...')
sleep(2)
computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
print(f'-COMPUTADOR escolheu {computador}')
msgVitoria = '\033[7;30;42m' + 'PARABÉNS! Você venceu o jogo!' + '\033[m'
msgDerrota = '\033[7;30;41m' + 'QUE PENA! Você perdeu o jogo!' + '\033[m'
if jogador != computador:
    if jogador == 'PEDRA':
        if computador == 'TESOURA':
            print(msgVitoria)
        else:
            print(msgDerrota)
    elif jogador == 'PAPEL':
        if computador == 'PEDRA':
            print(msgVitoria)
        else:
            print(msgDerrota)
    else:
        if computador == 'PAPEL':
            print(msgVitoria)
        else:
            print(msgDerrota)
else:
    print('\033[7;30;43m' + 'QUASE! Você empatou o jogo!' + '\033[m')