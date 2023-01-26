saque = int(input('Digite o valor para sacar: R$'))
i = 51
resto = 0
while True:
    i -= 1
    while i == 1 or i == 10 or i == 20 or i == 50:
        saque -= resto
        resto = i * (saque // i)
        print(f'{saque // i} cédulas de R${i}')
        i -= 1
    if i < 1:
        break