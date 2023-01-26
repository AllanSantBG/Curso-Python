resposta = 'S'
numeros = []
print('=' * 30)
while resposta not in 'N':
    num = float(input('Digite um número: '))
    resposta = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if resposta not in 'SN':
        print('Valor inválido, tente novamente')
    else:
        numeros.append(num)
    print('=' * 30)
print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Os números digitados em ordem descrescente: {numeros}')
if 5 in numeros:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')