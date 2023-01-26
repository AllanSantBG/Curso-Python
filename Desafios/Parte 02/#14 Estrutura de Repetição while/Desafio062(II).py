progressao = int(input('Digite o 1º termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
termos = int(input('Digite o número de termos da P.A.: '))
termosCont = 0
i = 0
while i < termos :
    i += 1
    print(progressao, end=', ')
    progressao += razao
    if i == termos:
        print('...')
        i = 0
        resposta = int(input('Digite a quantidade de termos: '))
        if resposta == 0:
            i += termos
            print(f'Esta progressão contém {termosCont} termos')
        else:
            termos = resposta
            termosCont += termos