progressao = int(input('Digite o 1º termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
i = 0
while i < 10 :
    i += 1
    print(progressao, end=', ')
    progressao += razao
print('...')