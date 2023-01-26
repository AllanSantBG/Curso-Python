num = int(input('Digite um número inteiro: '))
fatorial = 1
print(num, end='! = ')
if num == 0:
    print(1)
while num > 0:
    print(num, end='')
    print(end=' x ' if num != 1 else f' = {fatorial}')
    fatorial *= num
    num -= 1