numeros = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), 
        int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))
print(f'O número 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O número 3 aparece pela primeira vez na {numeros.index(3) + 1}ª posição')
else:
    print(f'O número 3 não aparece em nenhuma posição')
print(f'Os números pares foram ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')