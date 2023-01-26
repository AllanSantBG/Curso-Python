termo2 = 1
termo1 = 0
termos = int(input('Digite a quantidade de termos: '))
while termos < 1:
    print('=' * 40, '\nValor incorreto, tente novamente')
    termos = int(input('Digite a quantidade de termos: '))
print('1, ', end='')
for i in range(1, termos):
    print(termo2, end=', ')
    i += 1
    termo1 = termo2 - termo1
    termo2 += termo1
print('...')