termoUm = int(input('Digite o 1º TERMO da P.A.: '))
razao = int(input('Digite a RAZÃO da P.A.: '))
print('(', end='')
for i in range(termoUm, razao * 10, razao):
    print(i, end=',')
print('...)')