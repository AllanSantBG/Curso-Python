from random import randint
tentativas = 0
print('Tente adivinhar o número que o computador escolheu!')
acerto = False
while not acerto:
    tentativas += 1
    numJogador = int(input('Digite um número de 0 até 10: '))
    numComputador = randint(0, 10)
    if numJogador != numComputador:
        print(f'Que pena! o número sorteado foi {numComputador}, tente novamente!')
    else:
        acerto = True
print(f'Parabéns! o número sorteado foi {numJogador}!, está correto!')
print(f'Foram necessarias {tentativas} tentativa(s) para acertar')