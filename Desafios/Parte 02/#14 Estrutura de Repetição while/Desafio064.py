cont = num = soma= 0
while num != 999:
    cont += 1
    num = float(input(f'Digite o {cont}º valor (999 = PARAR): '))
    soma += num
print(f'Você digitou {cont - 1} vezes, a soma dos valores foi {soma - 999}')