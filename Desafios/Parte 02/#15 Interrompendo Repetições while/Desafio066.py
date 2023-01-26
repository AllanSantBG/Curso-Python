cont = soma = 0
while True:
    num = float(input(f'Digite um valor (999 = PARAR): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} valores, a soma dos valores foi {soma}')