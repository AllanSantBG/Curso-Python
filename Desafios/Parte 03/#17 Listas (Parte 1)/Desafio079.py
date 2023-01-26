resposta = 'S'
numeros = []
while resposta not in 'N':
    num = float(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print('Este valor ja foi inserido, tente novamente')
    resposta = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if resposta not in 'SN':
        print('Valor inválido, tente novamente')
    print('=' * 30)
numeros.sort()
print(f'Os números digitados em ordem crescente: {numeros}')