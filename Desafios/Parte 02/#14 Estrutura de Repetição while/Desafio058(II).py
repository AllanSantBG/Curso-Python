from random import randint
from time import sleep
cont = 1
print('Tente adivinhar o número que o computador escolheu!')
numEscolhido = int(input('Digite um número de 0 até 10: '))
numSorteado = randint(0, 10)
print('Verificando...')
sleep(2)
while numSorteado != numEscolhido:
    cont += 1
    print(f'Que pena! o número sorteado foi {numSorteado}, tente novamente!')
    numEscolhido = int(input('Digite um número de 0 até 10: '))
    numSorteado = randint(0, 10)
    print('Verificando...')
    sleep(2)
print(f'Parabéns! o número sorteado foi {numSorteado}!, está correto!')
print(f'Foram necessarias {cont} tentativa(s) para acertar')