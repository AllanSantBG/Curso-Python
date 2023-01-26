progressao = int(input('Digite o 1º termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
termos = int(input('Digite o número de termos da P.A.: '))
termosCont = i = 0
while i < termos:
    i += 1
    if i != termos:
        print(progressao, end=', ')
    else:
        i = 0
        termosCont += termos
        print(progressao)
        print('-' * 40)
        termos = int(input('Digite o número de termos da P.A.: '))
    progressao += razao
print('=' * 40, f'\nA progressão aritmetica teve {termosCont} termos')