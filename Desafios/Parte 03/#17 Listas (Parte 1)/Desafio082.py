resposta = 'S'
numeros = []
numerosPares = []
numerosImpares = []
print('=' * 30)
while resposta not in 'N':
    num = float(input('Digite um número: '))
    resposta = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if resposta not in 'SN':
        print('Valor inválido, tente novamente')
    else:
        numeros.append(num)
        if num % 2 == 0:
            numerosPares.append(num)
        else:
            numerosImpares.append(num)
    print('=' * 30)
print(f'Lista completa: {numeros}')
print(f'Lista de pares: {numerosPares}')
print(f'Lista de ímpares: {numerosImpares}')