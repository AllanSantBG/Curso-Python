from random import randint
from time import sleep
print('-' * 50)
print('Tente adivinhar o número que escolhi de 0 a 5')
print('-' * 50)
numSorteado = randint(0, 5)
numEscolhido = int(input('Digite um número de 0 a 5: '))
print('Verificando...')
sleep(2)
if numEscolhido == numSorteado:
    print(f'Parabéns! Você acertou, o número sorteado foi {numSorteado}!')
else:
    print(f'Que pena! Você errou, o número sorteado foi {numSorteado}!')
