cont = 0
soma = 0
for i in range(1, 7):
    num = int(input(f'Digite {i}º NÚMERO INTEIRO: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f'A soma do(s) {cont} NÚMERO(S) PAR(ES) é igual a {soma}')