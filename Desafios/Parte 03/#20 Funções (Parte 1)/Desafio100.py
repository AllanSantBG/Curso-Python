from random import randint

def sorteia():
    print(f'Os números sorteados foram ', end='')
    for i in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
        print(num, end=' ')
def somarPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'\nA soma dos valores pares sorteados é igual a {soma}')


numeros = list()
sorteia()
somarPar(numeros)